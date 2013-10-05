TITLE kdr.mod   Potassium delayed rectifier current as described by Traub et al. 1991

COMMENT
RD Traub et al. 1991 J. Neurophysiol.
"A Model of a CA3 Hippocampal Pyramidal Nueron Incorporating Voltage-Clamp Data on Intrinsic Conductances"
Adult guinea pig CA3 pyramidal cells
Potassium delayed rectifier current
Y Yamamura 5 October, 2013
ENDCOMMENT

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
	(mS) = (millisiemens)
}

NEURON {	::::: Interface with NEURON
	SUFFIX kdr
	USEION k READ ek WRITE ik
	RANGE gkbar
}

PARAMETER {
	gkbar = 15.0 (mS/cm2)	:::: Value for soma in original model
}

ASSIGNED {
	v		(mV)
	ek		(mV)
	ik	 	(mA/cm2)
	nalpha	(/ms)
	nbeta	(/ms)
}

STATE {		::::: Unknowns to be solved in BREAKPOINT
	n
}

BREAKPOINT {	::::: Must be placed before DERIVATIVE block!?
	SOLVE states METHOD cnexp	::::: Todo Investigate integration method.
	ik = gkbar*n*n*n*n*(v - ek)	::::: Only one n in original model?
}

UNITSOFF	::::: Units get in way of calculating rates as we've seen in Brian.
PROCEDURE rates(v (mV)) {	::::: Set rate constant values.
	nalpha	= (0.016*(35.1 - v)) / (exp((35.1 - v)/5) - 1)
	nbeta	= 0.25*exp((20.0 - v)/40)
}
UNITSON
	
DERIVATIVE states {
	rates(v)	::::: Procedure's side effect is setting rate consts.
	n'	= nalpha*(1-n) - nbeta*n
}

INITIAL {
	rates(v) ::::: Calculate malpha etc. for current v.
	n = nalpha/(nalpha+nbeta) ::::: ninf
}
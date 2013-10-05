TITLE na.mod   Sodium current as described by Traub et al. 1991

COMMENT
RD Traub et al. 1991 J. Neurophysiol.
"A Model of a CA3 Hippocampal Pyramidal Nueron Incorporating Voltage-Clamp Data on Intrinsic Conductances"
Adult guinea pig CA3 pyramidal cells
Fast sodium current
Y Yamamura 5 October, 2013
ENDCOMMENT

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
	(S) = (siemens)
}

NEURON {	::::: Interface with NEURON
	SUFFIX traub
	USEION na READ ena WRITE ina
	USEION k READ ek WRITE ik
	NONSPECIFIC_CURRENT il
	RANGE gnabar, gkbar, gl, el, gna, gk
	GLOBAL phi
}

PARAMETER {
	gnabar = 0.030 (S/cm2)	:::: Value for soma in original model
	gkbar = 0.015  (S/cm2)
	gl = 0.0003    (S/cm2)
	el = -65     (mV)
}

STATE {		::::: Unknowns to be solved in BREAKPOINT
	m h n
}

ASSIGNED {
	v	(mV)
	celsius (degC)
	ena	(mV)
	ek	(mV)
	gna	(S/cm2)
	gk	(S/cm2)

	ina 	(mA/cm2)
	ik	(mA/cm2)
	il	(mA/cm2)
	
	malpha	(/ms)
	mbeta	(/ms)
	halpha	(/ms)
	hbeta	(/ms)
	nalpha 	(/ms)
	nbeta	(/ms)

	phi
}

BREAKPOINT {	::::: Must be placed before DERIVATIVE block!?
	SOLVE states METHOD cnexp	::::: Todo Investigate integration method.
	gna = gnabar*m*m*m*h ::::: Only 2 m's in original model?
	ina = gna*(v - ena) ::::: Only 2 m's in original model?
	gk  = gkbar*n*n*n*n
	ik  = gk*(v - ek)
	il  = gl*(v - el)
}

INITIAL {
	rates(v) ::::: Calculate malpha etc. for current v.
	m = malpha/(malpha+mbeta) ::::: minf
	h = halpha/(halpha+hbeta) ::::: hinf
	n = nalpha/(nalpha+nbeta) ::::: ninf
}
	
DERIVATIVE states {
	rates(v)	::::: Procedure's side effect is setting rate consts.
	m'	= phi*(malpha*(1-m) - mbeta*m)
	h'	= phi*(halpha*(1-h) - hbeta*h)
	n'	= phi*(nalpha*(1-n) - nbeta*n)
}

UNITSOFF	::::: Units get in way of calculating rates as we've seen in Brian.
PROCEDURE rates(v (mV)) {	::::: Set rate constant values.
	malpha	= (0.32*(13.1 - v)) / (exp((13.1 - v)/4) - 1)
	mbeta	= ((-0.28)*(40.1 - v)) / (exp((40.1 - v)/(-5)) - 1)
	halpha	= 0.128*exp((17.0 - v)/18)
	hbeta	= 4 / (exp((40.0 - v)/5) + 1)
	nalpha	= (0.016*(35.1 - v)) / (exp((35.1 - v)/5) - 1)
	nbeta	= 0.25*exp((20.0 - v)/40)
	phi	= 3^((celsius - 37)/10)
}
UNITSON
TITLE na.mod   Sodium current as described by Traub et al. 1991

COMMENT
Traub RD et al. 1991 J. Neurophysiol.
"A Model of a CA3 Hippocampal Pyramidal Nueron Incorporating Voltage-Clamp Data on Intrinsic Conductances"
Adult guinea pig CA3 pyramidal cells
Fast sodium current
Y Yamamura 5 October, 2013
ENDCOMMENT

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
	(mS) = (millisiemens)
}

NEURON {	::::: Interface with NEURON
	SUFFIX na
	USEION na READ ena WRITE ina
	RANGE gnabar
}

PARAMETER {
	gmax = 30.0 (mS/cm2)	:::: Value for soma in original model
}

ASSIGNED {
	v		(mV)
	ena		(mV)
	ina 	(mA/cm2)
	malpha	(/ms)
	mbeta	(/ms)
	halpha	(/ms)
	hbeta	(/ms)
}

STATE {		::::: Unknowns to be solved in BREAKPOINT
	m h
}

UNITSOFF	::::: Units get in way of calculating rates as we've seen in Brian.
PROCEDURE rates(v (mV)) {	::::: Set rate constant values.
	malpha	= (0.32*(13.1 - v)) / (exp((13.1 - v)/4) - 1)
	mbeta	= ((-0.28)*(40.1 - v)) / (exp((40.1 - v)/(-5)) - 1)
	halpha	= 0.128*exp((17.0 - v)/18)
	hbeta	= 4 / (exp((40.0 - v)/5) + 1)
UNITSON
	
DERIVATIVE states {
	rates(v)	::::: Procedure's side effect is setting rate consts.
	m'	= malpha*(1-m) - mbeta*m
	h'	= halpha*(1-h) - hbeta*h
}

BREAKPOINT {
	SOLVE states METHOD cnexp	::::: Todo Investigate integration method.
	ina = gnabar*m*m*m*h*(v - ena)
}

INITIAL {
	rates(v) ::::: Calculate malpha etc. for current v.
	m = malpha/(malpha+mbeta) ::::: minf
	h = halpha/(halpha+hbeta) ::::: hinf
}
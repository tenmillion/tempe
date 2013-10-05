TITLE leak.mod	Passive membrane channel

UNITS {
	(mV) = (millivolt)
	(mA) = (milliamp)
	(mS) = (millisiemens)
}

NEURON {
	SUFFIX leak
	NONSPECIFIC_CURRENT il
	RANGE gl, el
}

PARAMETER {
	gl = 0.1	(mS/cm2)
}

ASSIGNED {
	v	(mV)
	el	(mV)
	il	(mA/cm2)
}

BREAKPOINT {
	il	= gl*(v - el)
}
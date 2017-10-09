def test_toAssembly():
    assert toAssembly(189) == "ADD 89"
    assert toAssembly(232) == "SUB 32"
    assert toAssembly(323) == "STA 23"
    assert toAssembly(501) == "LDA 1"
    assert toAssembly(622) == "BRA 22"
    assert toAssembly(743) == 'BRZ 43'
    assert toAssembly(901) == 'INP'
    assert toAssembly(902) == 'OUT'
    assert toAssembly(000) == 'HLT'
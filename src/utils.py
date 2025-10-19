def write_extxyz(path, positions_T, box, species="Ar"):
    """
    OVITO や ASE が読める Extended XYZ。
    コメント行に Lattice と Properties を記述。
    """
    T, N, _ = positions_T.shape
    Lx, Ly, Lz = box
    if isinstance(species, str):
        species = [species] * N

    lattice = f"{Lx} 0 0 0 {Ly} 0 0 0 {Lz}"
    with open(path, "w") as f:
        for t in range(T):
            f.write(f"{N}\n")
            f.write(
                f'Lattice="{lattice}" Properties=species:S:1:pos:R:3 pbc="T T T" Time={t}\n'
            )
            for i in range(N):
                x, y, z = positions_T[t, i]
                f.write(f"{species[i]} {x:.6f} {y:.6f} {z:.6f}\n")
    print(f"Wrote Extended XYZ: {path}")

import numpy as np

# Spannung Mittelwert
# sig_m
# Spannung Aplitude
# sig_a

# Spannungsverhaeltnis
# R = sig_m - sig_a

# 3.1 Spannungskennwerte
# 3.1.1 Nichtgeschweisste Bauteile


def get_eq_stress(
    sigmas, stress_type="principal", state="3d", material="ductile"
):
    """Compute von Mises stress depending on state (2D or 3D) and material elasticity.
    sigmas     tuple       depending on state and type principal or stress component
    sig_type   'principal', 'component'
    state      '2d': plane stress state
               '3d': 3D stress state
    """
    if material == "ductile":
        if state == "2d":
            if stress_type == "principal":
                sig_1, sig_2 = sigmas
                return np.sqrt(sig_1 ** 2 - sig_1 * sig_2 + sig_2 ** 2)
            else:  # stress components
                sig_x, sig_y, tau_zx = sigmas
                return np.sqrt(sig_x ** 2 - sig_x * sig_y + sig_y ** 2 + 3 * tau_zx**2)


if __name__ == "__main__":
    sig_v = get_eq_stress((20, 60), stress_type='principal', state='2d')
    print(f"Von Mises stress equals {sig_v:0.1f} MPa.")

    assert(get_eq_stress((20, 60), stress_type='principal', state='2d')) # 50.9
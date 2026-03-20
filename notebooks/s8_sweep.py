"""
S8 (Ouroboros) parameter sweep figure.
Generates a 2-panel figure:
  A) T(t) trajectories for varying recovery fraction rf
  B) Heatmap of collapse cycle count vs (rf, delta)
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import pathlib

figures_dir = pathlib.Path(__file__).resolve().parent.parent / "figures"
figures_dir.mkdir(parents=True, exist_ok=True)

# ── S8 baseline params (from notebook, authoritative) ──
S8_BASE = dict(r=0.0015, R0=800, delta=1.3, cf=0.6, rd=70, rf=0.35, h=0.0)
LIFESPAN = 1000


def simulate_run_deterministic(r, R0, delta, cf, rd, rf, h):
    """Single deterministic run (no stochastic noise)."""
    T = 1.0
    R = R0
    in_c = False
    timer = 0
    tech_ts = np.empty(LIFESPAN)
    res_ts = np.empty(LIFESPAN)
    cycles = 0

    for t in range(LIFESPAN):
        if in_c:
            timer += 1
            if timer >= rd:
                R = R0 * rf
                in_c = False
                timer = 0
        else:
            T += r
            R -= delta
            if R <= 0:
                R = 0
                in_c = True
                timer = 0
                T *= cf
                cycles += 1
        tech_ts[t] = T
        res_ts[t] = R

    duty_cycle = np.sum(res_ts > 0) / LIFESPAN
    return tech_ts, res_ts, cycles, duty_cycle


# ── Style setup ──
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.edgecolor": "black",
    "axes.labelcolor": "black",
    "xtick.color": "black",
    "ytick.color": "black",
    "text.color": "black",
    "axes.facecolor": "white",
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

fig = plt.figure(figsize=(12, 5))
gs = GridSpec(1, 2, figure=fig, wspace=0.35)

# ── Panel A: T(t) trajectories for varying rf ──
ax1 = fig.add_subplot(gs[0])
rf_values = [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50, 0.60]
cmap = plt.cm.viridis
colors = [cmap(i / (len(rf_values) - 1)) for i in range(len(rf_values))]
ticks = np.arange(LIFESPAN)

for rf_val, color in zip(rf_values, colors):
    tech, _, cycles, _ = simulate_run_deterministic(
        S8_BASE["r"], S8_BASE["R0"], S8_BASE["delta"],
        S8_BASE["cf"], S8_BASE["rd"], rf_val, S8_BASE["h"]
    )
    label = f"$r_f$ = {rf_val:.2f} ({cycles} cycles)"
    lw = 2.0 if rf_val == S8_BASE["rf"] else 1.0
    ls = "-" if rf_val == S8_BASE["rf"] else "-"
    ax1.plot(ticks, tech, color=color, lw=lw, ls=ls, label=label)

ax1.set_xlabel("t (yrs)")
ax1.set_ylabel("Tech, T(t)")
ax1.set_title("S8 Tech Trajectories: Varying $r_f$")
ax1.legend(fontsize=7, loc="upper left")
ax1.text(-0.08, 1.08, "A)", transform=ax1.transAxes,
         fontsize=14, fontweight="bold", va="top")
for spine in ax1.spines.values():
    spine.set_visible(True)
    spine.set_color("black")
    spine.set_linewidth(0.8)

# ── Panel B: Heatmap of cycles vs (rf, delta) ──
ax2 = fig.add_subplot(gs[1])

rf_range = np.arange(0.05, 0.71, 0.025)
delta_range = np.arange(0.5, 2.51, 0.1)
cycle_grid = np.zeros((len(delta_range), len(rf_range)))

for i, d in enumerate(delta_range):
    for j, rf in enumerate(rf_range):
        _, _, cyc, _ = simulate_run_deterministic(
            S8_BASE["r"], S8_BASE["R0"], d,
            S8_BASE["cf"], S8_BASE["rd"], rf, S8_BASE["h"]
        )
        cycle_grid[i, j] = cyc

im = ax2.pcolormesh(
    rf_range, delta_range, cycle_grid,
    cmap="YlOrRd", shading="nearest"
)
cbar = fig.colorbar(im, ax=ax2, label="Number of collapse cycles")
ax2.set_xlabel("Recovery fraction $r_f$")
ax2.set_ylabel("Depletion rate $\\delta$")
ax2.set_title("S8 Collapse Cycles: $r_f$ vs $\\delta$")

# Mark baseline
ax2.plot(S8_BASE["rf"], S8_BASE["delta"], "k*", markersize=12,
         markeredgecolor="white", markeredgewidth=0.5, label="Baseline")
ax2.legend(fontsize=8, loc="upper right")

ax2.text(-0.08, 1.08, "B)", transform=ax2.transAxes,
         fontsize=14, fontweight="bold", va="top")
for spine in ax2.spines.values():
    spine.set_visible(True)
    spine.set_color("black")
    spine.set_linewidth(0.8)

plt.tight_layout()
out = figures_dir / "s8_parameter_sweep.png"
plt.savefig(out, dpi=300, bbox_inches="tight")
print(f"Saved: {out}")
print(f"rf_range: {rf_range[0]:.2f} to {rf_range[-1]:.2f}, delta_range: {delta_range[0]:.1f} to {delta_range[-1]:.1f}")
print(f"Cycle grid min={cycle_grid.min()}, max={cycle_grid.max()}")

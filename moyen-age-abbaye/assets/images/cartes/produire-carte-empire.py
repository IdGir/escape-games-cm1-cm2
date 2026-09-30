import geopandas as gpd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.ops import unary_union

monde = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
terres = unary_union(monde.geometry)

# Étendue approximative de l'empire carolingien vers 814, dessinée à partir
# des contours actuels : France, Benelux, Suisse, Autriche, Slovénie,
# Germanie jusqu'à l'Elbe, Italie du nord et du centre jusqu'à Rome,
# marche d'Espagne (Catalogne). Limites simplifiées.
from shapely.geometry import box
europe = box(-12, 35, 22, 58)
def pays(nom): return unary_union(monde[monde.name == nom].geometry).intersection(europe)
morceaux = [pays(n) for n in ["France","Belgium","Netherlands","Luxembourg","Switzerland","Austria","Slovenia"]]
morceaux.append(pays("Germany").intersection(box(-12, 35, 13.2, 58)))
morceaux.append(pays("Italy").intersection(box(-12, 41.85, 22, 58)))
morceaux.append(pays("Spain").intersection(box(0.2, 40.6, 3.6, 43.5)))
empire_terre = unary_union(morceaux)

fig, ax = plt.subplots(figsize=(10, 7.2), dpi=120)
fig.patch.set_facecolor("#fbf3dd")
ax.set_facecolor("#cfe3ee")                                   # mer
monde.plot(ax=ax, color="#e6dcc3", edgecolor="#9c8a64", linewidth=.7)   # terres
gpd.GeoSeries([empire_terre]).plot(ax=ax, color="#c9a227", alpha=.8, edgecolor="#7d4a12", linewidth=2.0, hatch="//")

villes = [("Aix-la-Chapelle", 6.08, 50.77, "left", 6, 4),
          ("Rome", 12.48, 41.90, "left", 6, -14),
          ("Reims", 4.03, 49.26, "right", -7, 2),
          ("Paris", 2.35, 48.86, "right", -7, -12)]
for nom, lon, lat, ha, dx, dy in villes:
    ax.plot(lon, lat, "o", ms=7, color="#7d1818", mec="#3b0d0d", zorder=5)
    ax.annotate(nom, (lon, lat), textcoords="offset points", xytext=(dx, dy), ha=ha,
                fontsize=12, fontweight="bold", color="#2b1d10", zorder=6,
                bbox=dict(boxstyle="round,pad=.18", fc="#fbf3dd", ec="none", alpha=.85))

mers = [("OCÉAN\nATLANTIQUE", -8.5, 45.5, 13), ("MER DU NORD", 3.0, 56.0, 11),
        ("MER MÉDITERRANÉE", 8.0, 38.4, 11)]
for t, lon, lat, s in mers:
    ax.text(lon, lat, t, fontsize=s, color="#2c5a75", ha="center", va="center", style="italic")
for t, lon, lat in [("ESPAGNE", -3.5, 40.5), ("ITALIE", 14.5, 40.5), ("ANGLETERRE", -1.5, 52.6)]:
    ax.text(lon, lat, t, fontsize=10, color="#6b6152", ha="center", va="center")

# Légende
ax.plot([], [], "s", ms=14, color="#c9a227", mec="#7d4a12", label="L'empire de Charlemagne vers 814")
ax.plot([], [], "o", ms=8, color="#7d1818", mec="#3b0d0d", label="Villes citées dans le jeu")
ax.legend(loc="lower left", fontsize=11, framealpha=.92, facecolor="#fbf3dd", edgecolor="#9c8a64")

ax.set_xlim(-12, 21); ax.set_ylim(35.5, 57.5)
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_edgecolor("#9c8a64")
ax.set_title("L'empire de Charlemagne vers 814", fontsize=17, fontweight="bold", color="#16296b", pad=12)
fig.text(.5, .040, "Aix-la-Chapelle : la capitale de Charlemagne. Rome : le couronnement du 25 décembre 800.",
         ha="center", fontsize=9.5, color="#2b1d10")
fig.text(.5, .015, "Carte simplifiée dessinée pour le jeu, d'après les contours actuels : les limites de l'empire sont approximatives. "
                   "Fond de carte : Natural Earth (domaine public).",
         ha="center", fontsize=8, color="#6b6152")
fig.subplots_adjust(left=.02, right=.98, top=.93, bottom=.085)
fig.savefig("e2-3.jpg", pil_kwargs={"quality":88}, facecolor=fig.get_facecolor())
print("ok")

import json, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib import font_manager as fm
import sys
D = sys.argv[1]; OUT = sys.argv[2]
NAVY, GOLD, CREAM, GREY, RED, GREEN = "#1B3A6B", "#B8962E", "#F7F5F0", "#C9C4B8", "#A23B2A", "#3F7D58"
plt.rcParams.update({"font.family": "Inter", "font.size": 11, "axes.edgecolor": "#8A8577", "text.color": NAVY,
                     "axes.labelcolor": NAVY, "xtick.color": "#5A5649", "ytick.color": "#5A5649", "svg.fonttype": "none"})
k = {r["indicador"]: r for r in json.load(open(f"{D}/kpis.json"))}
esc = json.load(open(f"{D}/escaloes.json"))
dist = json.load(open(f"{D}/distritos.json"))
pt = lambda v, d=1: f"{v:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", " ")

def save(fig, name):
    fig.savefig(f"{OUT}/{name}.svg", facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0.25)
    fig.savefig(f"{OUT}/{name}.png", dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)

# 1 avaliação
tot = k["modelos_acordo"]["valor"]; sub = k["subavaliados"]["valor"]; sob = k["sobreavaliados"]["valor"]; jus = tot - sub - sob
fig, ax = plt.subplots(figsize=(9, 2.6), facecolor=CREAM); ax.set_facecolor(CREAM)
left = 0
for v, c, lab in [(sub, GREEN, "Abaixo do valor"), (jus, GREY, "Preço alinhado"), (sob, RED, "Acima do valor")]:
    ax.barh(0, v, left=left, color=c, height=0.55, edgecolor=CREAM, linewidth=2)
    ax.text(left + v / 2, 0, f"{pt(v/tot*100)}%", ha="center", va="center", color="white" if c != GREY else NAVY, fontsize=13, fontweight="bold")
    ax.text(left + v / 2, -0.52, f"{lab}\n{pt(v,0)} imóveis", ha="center", va="top", fontsize=9.5)
    left += v
ax.set_xlim(0, tot); ax.set_ylim(-1.05, 0.42); ax.axis("off")
ax.set_title(f"Preço pedido vs. valor estimado · {pt(tot,0)} imóveis com avaliação fiável", loc="left", fontsize=12, fontweight="bold", color=NAVY)
save(fig, "grafico-1-preco-vs-valor")

# 2 escalões
fig, ax = plt.subplots(figsize=(9, 4.6), facecolor=CREAM); ax.set_facecolor(CREAM)
labs = [e["escalao"] for e in esc]; n = [e["imoveis"] for e in esc]; y = [e["yield"] for e in esc]
ax.bar(labs, n, color=NAVY, alpha=.85, width=.55)
for i, v in enumerate(n): ax.text(i, v / 2, pt(v, 0), ha="center", va="center", fontsize=10, color="white", fontweight="bold")
ax.set_ylabel("Imóveis no escalão"); ax.spines[["top", "right"]].set_visible(False)
ax2 = ax.twinx(); ax2.plot(labs, y, color=GOLD, lw=2.5, marker="o", ms=7)
for i, v in enumerate(y): ax2.text(i, v + .06, f"{pt(v)}%", ha="center", color=GOLD, fontweight="bold", fontsize=10)
ax2.set_ylim(2.6, 4.0); ax2.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: pt(v))); ax2.set_ylabel("Yield bruta mediana (%)", color=GOLD); ax2.spines[["top"]].set_visible(False)
ax.set_xlabel("Escalão de preço pedido (€/m²)")
ax.set_title("Quanto mais caro o m², menor a rentabilidade do arrendamento", loc="left", fontsize=12, fontweight="bold")
fig.tight_layout(); save(fig, "grafico-2-yield-por-escalao")

# 3 distritos
d = sorted(dist, key=lambda r: r["preco_m2"])
fig, ax = plt.subplots(figsize=(9, 4.8), facecolor=CREAM); ax.set_facecolor(CREAM)
cols = [GOLD if r["distrito"] in ("Porto", "Braga") else NAVY for r in d]
ax.barh([f'{r["distrito"]} ({r["imoveis"]})' for r in d], [r["preco_m2"] for r in d], color=cols, height=.6)
for i, r in enumerate(d): ax.text(r["preco_m2"] + 40, i, f'{pt(r["preco_m2"],0)} €', va="center", fontsize=9.5)
ax.spines[["top", "right"]].set_visible(False); ax.set_xlim(0, 4900); ax.set_xlabel("Preço pedido mediano (€/m²) · entre parênteses, nº de imóveis")
ax.set_title("Preço pedido por distrito · Norte em destaque", loc="left", fontsize=12, fontweight="bold")
fig.tight_layout(); save(fig, "grafico-3-distritos")

# 4 cartão redes 1080x1350
fig = plt.figure(figsize=(5.4, 6.75), facecolor=NAVY)
fig.text(.08, .9, "RADAR DE MERCADO · CORDIAL LEVEL", color=GOLD, fontsize=11, fontweight="bold")
fig.text(.08, .84, "Semana de 22 a 28 de outubro", color=CREAM, fontsize=10)
fig.text(.08, .60, f"{pt(k['sobreavaliados']['pct'])}%", color=CREAM, fontsize=64, fontfamily="DejaVu Serif")
fig.text(.08, .44, "dos imóveis à venda pedem\nacima do valor estimado", color=CREAM, fontsize=17, linespacing=1.3)
fig.text(.08, .33, f"Apenas {pt(k['subavaliados']['pct'])}% estão abaixo do valor.\nYield bruta mediana: {pt(k['yield']['valor'])}%", color=GOLD, fontsize=12, linespacing=1.5)
fig.text(.08, .12, "Análise reservada a parceiros e investidores", color=CREAM, fontsize=9.5)
fig.text(.08, .07, "Cordial Level | CENTURY 21 Arquitectos · AMI 11414", color=CREAM, fontsize=9)
fig.text(.08, .035, "Fonte: PrivateMarkets.pt (preços pedidos, 10 distritos)", color=GREY, fontsize=7.5)
fig.savefig(f"{OUT}/cartao-redes-1080x1350.png", dpi=200, facecolor=NAVY); plt.close(fig)
print("ok")

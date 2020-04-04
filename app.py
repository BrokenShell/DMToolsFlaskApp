from flask import Flask, request, render_template
from MonsterGen import Monster, random_trap, Npc
from DungeonLib import Dungeon
from Fortuna import distribution_range, front_poisson


app = Flask(__name__)


@app.route('/')
@app.route("/monster")
def monster():
    return render_template(
        "monster.html",
        monster=Monster(distribution_range(
            front_poisson, -3, 30,
        )).to_dict().items(),
    )


@app.route("/npc")
def npc():
    return render_template(
        "npc.html",
        npc=Npc().to_dict().items(),
    )


@app.route("/trap")
def trap():
    return render_template(
        "trap.html",
        trap=random_trap(distribution_range(
            front_poisson, -3, 30,
        )).to_dict().items(),
    )


@app.route("/dungeon-results", methods=['POST'])
def dungeon_results():
    return render_template(
        "dungeon-results.html",
        dungeon=Dungeon(
            dungeon_name=request.form.get('DungeonName') or None,
            cr=int(request.form.get('cr')),
            dungeon_levels=int(request.form.get("num_levels")),
            rooms_per_level=int(request.form.get("num_rooms")),
            make_traps=bool(request.form.get("traps")),
        ),
    )


@app.route("/dungeon")
def dungeon():
    return render_template("dungeon.html")


if __name__ == '__main__':
    app.run()

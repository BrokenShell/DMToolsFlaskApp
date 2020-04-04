from flask import Flask, request, render_template
from MonsterGen import Monster, random_trap, Npc
from DungeonLib import Dungeon


app = Flask(__name__)


@app.route('/')
@app.route("/monster")
def monster():
    return render_template("monster.html")


@app.route("/monster-results", methods=['POST'])
def monster_results():
    return render_template(
        "monster-results.html",
        monster=Monster(
            cr=int(request.form.get('cr')),
            monster_type=request.form.get('monstertype'),
        ).to_dict().items(),
    )


@app.route("/npc")
def npc():
    return render_template(
        "npc.html",
        npc=Npc().to_dict().items(),
    )


@app.route("/trap")
def trap():
    return render_template("trap.html")


@app.route("/trap-results", methods=['POST'])
def trap_results():
    return render_template(
        "trap-results.html",
        trap=random_trap(
            cr=int(request.form.get('cr')),
            dam_type=request.form.get('damagetype'),
        ).to_dict().items(),
    )


@app.route("/dungeon")
def dungeon():
    return render_template("dungeon.html")


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


if __name__ == '__main__':
    app.run()

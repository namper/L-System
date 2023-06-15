import turtle as CG
from time import sleep
import random


class l_system:
    """
    init(_ turtleMouse ,  _ axioms , _ speed , _ evolution , _ angle)
    This Class will handle evey sierpensky algorithm
    Input will be n(evolution number) & axiom ---------------------->
    Each algorithm has different evolution value (n)
    Each algorithm has different axiom
    Each algorithm has different angle
    Class
    """

    def __init__(self, turtleMouse, axioms, speed, evolution, angle):
        self.t = turtleMouse
        self.axioms = axioms
        self.evolution = evolution
        self.angle = angle
        self.hexcolors = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
        ]
        self.t.speed(speed)
        self.ignoredPunctuation = ["'", "[", "]"]
        self.trasnofrmation = {
            "F": "F+F-F-F+F",
            "A": "B-A-B",
            "B": "A+B+A",
            "X": "YA+XA+Y",
            "Y": "XA-YA-X",
            "Q": "QQ",
            "Z": "Z-Q+Z+Q-Z",
        }
        self.action = {
            "+": self.t.left,
            "-": self.t.right,
            "F": self.t.forward,
            "G": self.t.forward,
            "A": self.t.forward,
            "B": self.t.forward,
            "Z": self.t.forward,
            "Q": self.t.forward,
        }
        self.value = {
            "F": 10,
            "G": 10,
            "A": 1,
            "B": 1,
            "Q": 5,
            "Z": 5,
        }
        self.growAxiomAndDie()
        self.resetAndGenerateNewColor()

    def growAxiomAndDie(self):
        for eachEvolution in range(self.evolution):
            executable = []  # Array for generateing l_system code
            """ do this nTH time"""
            for eachAxiom in self.axioms:
                if eachAxiom not in self.ignoredPunctuation:
                    if eachAxiom in self.trasnofrmation.keys():
                        executable.append(self.trasnofrmation[eachAxiom])
                    else:
                        executable.append(eachAxiom)
            # ReSetting Axioms Value
            self.axioms = str(executable)
        # Checking Axioms And Drawing On Context
        for axiom in self.axioms:
            if axiom in self.action.keys():
                if axiom == "+" or axiom == "-":
                    self.action[axiom](self.angle)
                else:
                    self.action[axiom](self.value[axiom])
        sleep(4)  ## delay to show canvas

    def resetAndGenerateNewColor(self):
        # Randomly choose Atribute from self.hexcolors
        newColor = "#" + "".join([random.choice(self.hexcolors) for _ in range(6)])
        self.t.reset()
        self.t.clear()
        self.t.color(newColor)
        self.t.ht()


if __name__ == "__main__":
    """
    If file is not imported
    Run the script
    """
    window = CG.Screen()
    t = CG.Turtle()
    sleep(1)
    t.ht()
    # if turtle crushes exit
    try:
        # Koch curve ( arc )
        l_system(t, "F", 10000000, 3, 90)
        # Sierpenksy Triangle ( a.k.a mathemtaical beauty)
        l_system(t, "Z-Q-Q", 50000000, 6, -120)
        # Sierpensky ArrowHead Curve ( triangle )
        l_system(t, "A", 500000000, 8, 60)
    except Exception as e:
        print(e)

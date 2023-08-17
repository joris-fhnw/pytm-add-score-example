
from pytmlib import AbstractExercise
from pytmlib import Latex
from pytmlib import Output


#Test
class Exercise(AbstractExercise):
    @property
    def version(self) -> str:
        return "1.0.0"

    def start(self) -> Output:

        return self.output \
            .add_option_group(name='ja_nein',
                              label=Latex(r'Wollen Sie einen Score und somit eine Bestehungsnote erhalten?:'),
                              options=["Ja","Nein"],
                              inline=False) \
            .add_action('Abgabe', self.abgabe)

    def abgabe(self, ja_nein: str) -> Output:
        if ja_nein == "Ja":
            score = 1
            answ = f"super Sie haben bestanden und einen Score von {score} erhalten"
        else:
            score = 0
            answ = f"Sie haben leider nicht bestanden..."

        return self.output \
            .add_paragraph(Latex(f'{answ}')) \
            .add_action('Back to start',self.start)

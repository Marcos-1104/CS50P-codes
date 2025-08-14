from fpdf import FPDF
from fpdf.enums import XPos, YPos

class User:
    def __init__(self,user_name):
        self.user_name = user_name

    def make_shirt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font("helvetica", style="B", size=24)
        pdf.cell(w=0,h = 40,text = "CS50 Shirtificate", align = "C",new_x=XPos.LMARGIN,new_y=YPos.NEXT)

        pdf.image("shirtificate.png", x = "C", y = 60, w=180)

        pdf.set_text_color(255,255,255)
        pdf.set_font("helvetica", style="B", size=16)
        pdf.set_y(120)
        pdf.cell(w=0,text = f"{self.user_name} took CS50", align = "C")

        pdf.output("shirtificate.pdf")

def main():

    user = User(input("Name:"))
    user.make_shirt()

if __name__ == "__main__":
    main()




import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from collections import defaultdict
import pandas as pd

class CreatePDF:
    def __init__(self, data: dict):
        self.data_dict = defaultdict(lambda: "N/A", data)

    def to_pdf(self, filename=None):
        if filename is None:
            filename = f"{self.data_dict['stock_name']}.pdf"

        fig, ax = plt.subplots(figsize=(8.27, 11.69))
        ax.axis("tight")
        ax.axis("off")

        stock_name = self.data_dict["stock_name"]
        plt.suptitle(f"{stock_name} REPORT", fontsize=18, fontweight="bold", y=0.98, color="#000000")

        # Add the "about" paragraph above the table
        about_text = self.data_dict['about']
        fig.text(
            0.5, 0.89,  # X, Y position (Y just below the title)
            about_text,
            ha="center",
            va="top",
            wrap=True,
            fontsize=12,
            color="black"
        )

        custom_fields = [
            ("Console time", "time"),
            ("Current Value", "current_value"),
            ("Previous Close", "previous_close"),
            ("Day Range", "day_range"),
            ("Year Range", "year_range"),
            ("Market Cap", "market_cap"),
            ("Average Volume", "average_volume"),
            ("Primary Exchange", "primary_exchange"),
            ("CEO", "ceo"),
            ("Founded", "founded"),
            ("Website", "website"),
            ("Employees", "employees")
        ]

        table_rows = [[label, self.data_dict[key]] for label, key in custom_fields]

        table = ax.table(
            cellText=table_rows,
            colLabels=["Field", "Stock Data"],
            loc="center",
            cellLoc="center",
            colWidths=[0.4, 0.6]
        )
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1.2, 1.2)

        for (row, col), cell in table.get_celld().items():
            if row == 0:
                cell.set_text_props(weight="bold", color="white")
                cell.set_facecolor("#46b4a5")

        fig.text(
            0.5, 0.02,
            f"Generated on: {pd.Timestamp.now().strftime('%d/%m/%Y %H:%M:%S')}",
            ha="center",
            fontsize=9,
            color="gray"
        )

        with PdfPages(filename) as pdf:
            pdf.savefig(fig, bbox_inches="tight", dpi=300)
            plt.close()

# Example usage:
if __name__ == "__main__":
    data = {'stock_name': 'TAKE-TWO INTERACTIVE SOFTWARE, INC Common Stock',
            'about': "Take-Two Interactive Software, Inc. is an American video game holding company based in New York City founded by Ryan Brant in September 1993.\nThe company owns three major publishing labels, Rockstar Games, Zynga and 2K, which operate internal game development studios. Take-Two created the Private Division label to support publishing from independent developers, though it sold the label in 2024. The company also formed Ghost Story Games which was a former 2K studio under the name Irrational Games. The company acquired the developers Socialpoint, Playdots and Nordeus to establish itself in the mobile game market. The company also owns 50% of professional esports organization NBA 2K League through NBA Take-Two Media. Take-Two's combined portfolio includes franchises such as BioShock, Borderlands, Civilization, Grand Theft Auto, NBA 2K, WWE 2K, and Red Dead among others.\nAs of April 2025, it is one of the largest publicly traded game companies globally with an estimated market cap of US$41 billion. Wikipedia",
              'stock': 'TTWO', 'time': '15/06/2025 20:23:19', 'current_value': '$230.23', 'previous_close': '$234.46', 'day_range': '$229.59 - $235.80', 'year_range': '$135.24 - $240.78', 'market_cap': '42.04B USD', 'average_volume': '2.64M', 'p_e_ratio': '-', 'dividend_yield': '-', 'primary_exchange': 'NASDAQ', 'ceo': 'Strauss Zelnick', 'founded': 'Sep 30, 1993', 'website': 'take2games.com', 'employees': '12,928'}
    pdf_creator = CreatePDF(data)
    pdf_creator.to_pdf()
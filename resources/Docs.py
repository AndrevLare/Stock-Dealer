import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class CreatePDF:
    def __init__(self, data: dict):
        self.data_dict = data
        # Remove 'stock_name' from table data for clarity in the table
        self.table_data = {k: v for k, v in data.items() if k != 'stock_name'}
        self.df = pd.DataFrame(list(self.table_data.items()), columns=['Field', 'Value'])

    def to_pdf(self, filename='output.pdf'):
        # A4 size in inches: 8.27 x 11.69
        fig, ax = plt.subplots(figsize=(8.27, 11.69))
        ax.axis('tight')
        ax.axis('off')

        # Title from stock_name
        stock_name = self.data_dict.get('stock_name', 'Stock Report')
        plt.suptitle(f"{stock_name} REPORT", fontsize=18, fontweight='bold', y=0.98, color="#000000")

        # Table
        values_only = list(self.table_data.values())
        custom_labels = [
    "Console time", "Previous Close", "Day Range", "Year Range", "Market Cap",
    "Average Volume", "Primary Exchange", "CEO", "Founded", "Website", "Employees"
]
        # Combine custom labels and values into rows
        table_rows = list(zip(custom_labels, values_only))
        table = ax.table(
            cellText=table_rows,
            colLabels=["Field", "Stock Data"],
            loc='center',
            cellLoc='center',
            colWidths=[0.4, 0.6]
        )
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1.2, 1.2)

        # Style header
        for (row, col), cell in table.get_celld().items():
            if row == 0:
                cell.set_text_props(weight='bold', color='white')
                cell.set_facecolor("#46b4a5")

        # Footer with generation date
        fig.text(
            0.5, 0.02,
            f"Generated on: {pd.Timestamp.now().strftime('%d/%m/%Y %H:%M:%S')}",
            ha='center',
            fontsize=9,
            color='gray'
        )

        with PdfPages(filename) as pdf:
            pdf.savefig(fig, bbox_inches='tight', dpi=300)
            plt.close()

# Example usage:
if __name__ == "__main__":
    data = {
        'stock_name': 'COCA-COLA FEMSA',
        'time': '13/06/2025 21:59:03',
        'current_value': '$96.44',
        'previous_close': '$99.04',
        'day_range': '$96.44 - $98.55',
        'year_range': '$72.68 - $101.74',
        'market_cap': '20.32B USD',
        'average_volume': '268.44K',
        'primary_exchange': 'NYSE',
        'ceo': 'Ian M. Craig García',
        'founded': 'Oct 30, 1991',
        'website': 'coca-colafemsa.com',
        'employees': '118,683'
    }
    pdf_creator = CreatePDF(data)
    pdf_creator.to_pdf('test1.pdf')
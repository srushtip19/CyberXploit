from fpdf import FPDF


def generate_report(filename, content):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="CyberXploit Security Report", ln=True)
    pdf.ln(10)

    for line in content:
        pdf.multi_cell(0, 10, txt=str(line))

    pdf.output(filename)

    return filename
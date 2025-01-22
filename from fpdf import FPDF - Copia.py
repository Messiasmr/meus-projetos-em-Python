from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Respostas do Formulário", ln=True, align='C')
    
    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
    
    pdf_file = "respostas_formulario.pdf"
    pdf.output(pdf_file)
    
    return pdf_file

def send_email(pdf_file):
    from_email = "seu_email@gmail.com"
    to_email = "destinatario@gmail.com"
    subject = "Respostas do Formulário"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    attachment = open(pdf_file, "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    
    part.add_header('Content-Disposition', f"attachment; filename= {pdf_file}")
    
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    server.login(from_email, "sua_senha")
    
    text = msg.as_string()
    
    server.sendmail(from_email, to_email, text)
    
    server.quit()

# Exemplo de dados do formulário
data = {
    "Qual seu nome?": "Cris",
    "Qual sua idade?": "28",
    "Você possui pets?": "Sim",
    "Se sim, quais são as maiores preocupações com a saúde e bem-estar do seu pet?": "Alimentação e exercícios",
    "Como você se sente ao ter que leva-lo a um petshop?": "Preocupado",
    "O que mais valoriza em um petshop? (Atendimento, agendamento, produtos, preço?)": "Atendimento",
    "Quais são as maiores frustrações ao utilizar serviços de um petshop loja física e online?": "Preços altos",
    "Como pesquisa por produtos e serviços para pets?": "Online",
    "Quais são as opiniões de amigos e familiares sobre diferentes petshops?": "Variadas",
    "Quais são os tipos de comunicação que mais chamam a atenção?": "Promoções",
    "Quais são as necessidades de informação sobre cuidados com pets?": "Dicas de saúde",
    "Quais são os desejos em relação à experiência de compra?": "Facilidade"
}

pdf_file = generate_pdf(data)
send_email(pdf_file)

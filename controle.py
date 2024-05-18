from PyQt5 import uic, QtWidgets


def principal():
    salario = float(formulario.txtSalario.text())
    desconto = float(formulario.txtDescontos.text())
    resultado = salario - (desconto*salario/100)
    fgts = salario * 0.08
    formulario.lblResultado.setText(f'Salário líquido = R${resultado:.2f}\n'
                                    f'FGTS mensal = R${fgts:.2f}\n'
                                    f'FGTS anual (estimativa) = R${fgts*12:.2f}')


app = QtWidgets.QApplication([])  # cria var contendo widgets
formulario = uic.loadUi("main.ui")  # cria a variavel tela
formulario.btnCalcular.clicked.connect(principal)  # quando o botão for pressionado chama a função

formulario.show()  # carrega a tela
app.exec()  # carrega funções/widgets

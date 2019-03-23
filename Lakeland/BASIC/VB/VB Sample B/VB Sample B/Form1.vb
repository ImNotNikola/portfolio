Public Class frmCalcSalesTax

    Private Sub frmCalcSalesTax_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load

    End Sub

    Private Sub BtnCalc_Click(sender As System.Object, e As System.EventArgs) Handles BtnCalc.Click
        Dim sngPRICE As Single
        Dim sngRate As Single
        Dim sngSalesTax As Single
        sngPRICE = CSng(txtPrice.Text)
        sngRate = CSng(txtRate.Text)
        sngSalesTax = sngRate * sngPRICE
        txtSalesTax.Text = CStr(sngSalesTax)
    End Sub
End Class

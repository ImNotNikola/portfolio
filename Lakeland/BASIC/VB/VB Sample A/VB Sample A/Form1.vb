Public Class frmColor

    Private Sub frmColor_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load

    End Sub

    Private Sub btnDisplay_Click(sender As System.Object, e As System.EventArgs) Handles btnDisplay.Click
        lblResponse.Text = txtColor.Text + " is a great choice!"
    End Sub
End Class

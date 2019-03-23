<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class frmColor
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.txtColor = New System.Windows.Forms.TextBox()
        Me.lblResponse = New System.Windows.Forms.Label()
        Me.btnDisplay = New System.Windows.Forms.Button()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(40, 47)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(122, 13)
        Me.Label1.TabIndex = 0
        Me.Label1.Text = "Enter your favorite color:"
        '
        'txtColor
        '
        Me.txtColor.Location = New System.Drawing.Point(169, 47)
        Me.txtColor.Name = "txtColor"
        Me.txtColor.Size = New System.Drawing.Size(100, 20)
        Me.txtColor.TabIndex = 1
        '
        'lblResponse
        '
        Me.lblResponse.AutoSize = True
        Me.lblResponse.Location = New System.Drawing.Point(137, 120)
        Me.lblResponse.Name = "lblResponse"
        Me.lblResponse.Size = New System.Drawing.Size(25, 13)
        Me.lblResponse.TabIndex = 2
        Me.lblResponse.Text = "      "
        '
        'btnDisplay
        '
        Me.btnDisplay.Location = New System.Drawing.Point(87, 136)
        Me.btnDisplay.Name = "btnDisplay"
        Me.btnDisplay.Size = New System.Drawing.Size(75, 23)
        Me.btnDisplay.TabIndex = 3
        Me.btnDisplay.Text = "Display"
        Me.btnDisplay.UseVisualStyleBackColor = True
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(13, 13)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(68, 13)
        Me.Label2.TabIndex = 4
        Me.Label2.Text = "Nikola Kuhar"
        '
        'frmColor
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(284, 188)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.btnDisplay)
        Me.Controls.Add(Me.lblResponse)
        Me.Controls.Add(Me.txtColor)
        Me.Controls.Add(Me.Label1)
        Me.Name = "frmColor"
        Me.Text = "Favorite Color"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents txtColor As System.Windows.Forms.TextBox
    Friend WithEvents lblResponse As System.Windows.Forms.Label
    Friend WithEvents btnDisplay As System.Windows.Forms.Button
    Friend WithEvents Label2 As System.Windows.Forms.Label

End Class

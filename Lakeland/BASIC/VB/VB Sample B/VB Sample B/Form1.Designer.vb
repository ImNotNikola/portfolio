<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class frmCalcSalesTax
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
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.txtPrice = New System.Windows.Forms.TextBox()
        Me.txtRate = New System.Windows.Forms.TextBox()
        Me.txtSalesTax = New System.Windows.Forms.TextBox()
        Me.BtnCalc = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(12, 9)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(68, 13)
        Me.Label1.TabIndex = 0
        Me.Label1.Text = "Nikola Kuhar"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(92, 74)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(37, 13)
        Me.Label2.TabIndex = 1
        Me.Label2.Text = "Price: "
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(43, 104)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(86, 13)
        Me.Label3.TabIndex = 2
        Me.Label3.Text = "Sales Tax Rate: "
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Location = New System.Drawing.Point(72, 168)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(57, 13)
        Me.Label4.TabIndex = 3
        Me.Label4.Text = "Sales Tax:"
        '
        'txtPrice
        '
        Me.txtPrice.Location = New System.Drawing.Point(146, 67)
        Me.txtPrice.Name = "txtPrice"
        Me.txtPrice.Size = New System.Drawing.Size(100, 20)
        Me.txtPrice.TabIndex = 4
        '
        'txtRate
        '
        Me.txtRate.Location = New System.Drawing.Point(146, 97)
        Me.txtRate.Name = "txtRate"
        Me.txtRate.Size = New System.Drawing.Size(100, 20)
        Me.txtRate.TabIndex = 5
        '
        'txtSalesTax
        '
        Me.txtSalesTax.Location = New System.Drawing.Point(146, 161)
        Me.txtSalesTax.Name = "txtSalesTax"
        Me.txtSalesTax.ReadOnly = True
        Me.txtSalesTax.Size = New System.Drawing.Size(100, 20)
        Me.txtSalesTax.TabIndex = 6
        '
        'BtnCalc
        '
        Me.BtnCalc.Location = New System.Drawing.Point(292, 93)
        Me.BtnCalc.Name = "BtnCalc"
        Me.BtnCalc.Size = New System.Drawing.Size(75, 23)
        Me.BtnCalc.TabIndex = 7
        Me.BtnCalc.Text = "Calculate"
        Me.BtnCalc.UseVisualStyleBackColor = True
        '
        'frmCalcSalesTax
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(405, 262)
        Me.Controls.Add(Me.BtnCalc)
        Me.Controls.Add(Me.txtSalesTax)
        Me.Controls.Add(Me.txtRate)
        Me.Controls.Add(Me.txtPrice)
        Me.Controls.Add(Me.Label4)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Name = "frmCalcSalesTax"
        Me.Text = "Calculate Sales Tax"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents txtPrice As System.Windows.Forms.TextBox
    Friend WithEvents txtRate As System.Windows.Forms.TextBox
    Friend WithEvents txtSalesTax As System.Windows.Forms.TextBox
    Friend WithEvents BtnCalc As System.Windows.Forms.Button

End Class

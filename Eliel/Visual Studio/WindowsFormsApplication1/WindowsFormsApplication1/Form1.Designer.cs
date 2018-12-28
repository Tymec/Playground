namespace WindowsFormsApplication1
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Number1 = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.Number2 = new System.Windows.Forms.TextBox();
            this.Display = new System.Windows.Forms.TextBox();
            this.Result = new System.Windows.Forms.Label();
            this.plus = new System.Windows.Forms.Button();
            this.minus = new System.Windows.Forms.Button();
            this.multiply = new System.Windows.Forms.Button();
            this.divide = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // Number1
            // 
            this.Number1.Location = new System.Drawing.Point(12, 107);
            this.Number1.Name = "Number1";
            this.Number1.Size = new System.Drawing.Size(79, 20);
            this.Number1.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(24, 91);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Number 1";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(190, 91);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(53, 13);
            this.label2.TabIndex = 2;
            this.label2.Text = "Number 2";
            // 
            // Number2
            // 
            this.Number2.Location = new System.Drawing.Point(176, 107);
            this.Number2.Name = "Number2";
            this.Number2.Size = new System.Drawing.Size(79, 20);
            this.Number2.TabIndex = 3;
            // 
            // Display
            // 
            this.Display.Location = new System.Drawing.Point(77, 332);
            this.Display.Name = "Display";
            this.Display.Size = new System.Drawing.Size(127, 20);
            this.Display.TabIndex = 4;
            // 
            // Result
            // 
            this.Result.AutoSize = true;
            this.Result.Location = new System.Drawing.Point(119, 316);
            this.Result.Name = "Result";
            this.Result.Size = new System.Drawing.Size(37, 13);
            this.Result.TabIndex = 5;
            this.Result.Text = "Result";
            // 
            // plus
            // 
            this.plus.Location = new System.Drawing.Point(38, 175);
            this.plus.Name = "plus";
            this.plus.Size = new System.Drawing.Size(39, 23);
            this.plus.TabIndex = 6;
            this.plus.Text = "+";
            this.plus.UseVisualStyleBackColor = true;
            this.plus.Click += new System.EventHandler(this.button1_Click);
            // 
            // minus
            // 
            this.minus.Location = new System.Drawing.Point(193, 175);
            this.minus.Name = "minus";
            this.minus.Size = new System.Drawing.Size(38, 23);
            this.minus.TabIndex = 7;
            this.minus.Text = "-";
            this.minus.UseVisualStyleBackColor = true;
            this.minus.Click += new System.EventHandler(this.button2_Click);
            // 
            // multiply
            // 
            this.multiply.Location = new System.Drawing.Point(38, 221);
            this.multiply.Name = "multiply";
            this.multiply.Size = new System.Drawing.Size(39, 23);
            this.multiply.TabIndex = 8;
            this.multiply.Text = "*";
            this.multiply.UseVisualStyleBackColor = true;
            this.multiply.Click += new System.EventHandler(this.button3_Click);
            // 
            // divide
            // 
            this.divide.Location = new System.Drawing.Point(193, 221);
            this.divide.Name = "divide";
            this.divide.Size = new System.Drawing.Size(38, 23);
            this.divide.TabIndex = 9;
            this.divide.Text = "/";
            this.divide.UseVisualStyleBackColor = true;
            this.divide.Click += new System.EventHandler(this.button4_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(294, 379);
            this.Controls.Add(this.divide);
            this.Controls.Add(this.multiply);
            this.Controls.Add(this.minus);
            this.Controls.Add(this.plus);
            this.Controls.Add(this.Result);
            this.Controls.Add(this.Display);
            this.Controls.Add(this.Number2);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.Number1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox Number1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox Number2;
        private System.Windows.Forms.TextBox Display;
        private System.Windows.Forms.Label Result;
        private System.Windows.Forms.Button plus;
        private System.Windows.Forms.Button minus;
        private System.Windows.Forms.Button multiply;
        private System.Windows.Forms.Button divide;
    }
}


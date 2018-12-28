namespace WindowsFormsApplication6
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.Generate = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.location1 = new System.Windows.Forms.Button();
            this.Passwords = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // Generate
            // 
            this.Generate.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Bold);
            this.Generate.Location = new System.Drawing.Point(38, 285);
            this.Generate.Name = "Generate";
            this.Generate.Size = new System.Drawing.Size(190, 67);
            this.Generate.TabIndex = 0;
            this.Generate.Text = "Generate";
            this.Generate.UseVisualStyleBackColor = true;
            this.Generate.Click += new System.EventHandler(this.Generate_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.BackColor = System.Drawing.Color.Transparent;
            this.label1.Font = new System.Drawing.Font("Georgia", 15.5F, System.Drawing.FontStyle.Bold);
            this.label1.Location = new System.Drawing.Point(4, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(333, 25);
            this.label1.TabIndex = 1;
            this.label1.Text = "Random Password Generator";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.BackColor = System.Drawing.Color.Transparent;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 6F);
            this.label2.Location = new System.Drawing.Point(401, 369);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(60, 9);
            this.label2.TabIndex = 2;
            this.label2.Text = "Made by Tymek";
            // 
            // location1
            // 
            this.location1.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Bold);
            this.location1.Location = new System.Drawing.Point(61, 132);
            this.location1.Name = "location1";
            this.location1.Size = new System.Drawing.Size(140, 59);
            this.location1.TabIndex = 3;
            this.location1.Text = "Choose the location";
            this.location1.UseVisualStyleBackColor = true;
            this.location1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Passwords
            // 
            this.Passwords.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold);
            this.Passwords.FormattingEnabled = true;
            this.Passwords.ItemHeight = 16;
            this.Passwords.Location = new System.Drawing.Point(282, 73);
            this.Passwords.Name = "Passwords";
            this.Passwords.Size = new System.Drawing.Size(179, 292);
            this.Passwords.TabIndex = 4;
            this.Passwords.UseTabStops = false;
            this.Passwords.SelectedIndexChanged += new System.EventHandler(this.Passwords_SelectedIndexChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(462, 377);
            this.Controls.Add(this.Passwords);
            this.Controls.Add(this.location1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.Generate);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "Random Password Generator©";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button Generate;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button location1;
        private System.Windows.Forms.ListBox Passwords;
    }
}


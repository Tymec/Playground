using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int Result = int.Parse(Number1.Text) + int.Parse(Number2.Text);
            Display.Text = Result.ToString();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            int Result = int.Parse(Number1.Text) - int.Parse(Number2.Text);
            Display.Text = Result.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int Result = int.Parse(Number1.Text) * int.Parse(Number2.Text);
            Display.Text = Result.ToString();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                int Result = int.Parse(Number1.Text) / int.Parse(Number2.Text);
                Display.Text = Result.ToString();
            }
            catch(DivideByZeroException)
            {
                MessageBox.Show("Can not divide by zero!"); 
            }
        }
    }
}

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int A = int.Parse(Value1.Text), B = int.Parse(Value2.Text), C = int.Parse(Value3.Text);
            double X1, X2;
            double calculation = Math.Pow(B, 2) - 4 * A * C;
            if(calculation <0)
            {
            X1 = (-B + Math.Sqrt(-calculation)) / (2 * A);
            X2 = (-B - Math.Sqrt(-calculation)) / (2 * A);
            Result1.Text = X1.ToString() + "i";
            Result2.Text = X2.ToString() + "i";
            }
            else
            {
            X1 = (-B + Math.Sqrt(calculation)) / (2 * A);
            X2 = (-B - Math.Sqrt(calculation)) / (2 * A);
            Result1.Text = X1.ToString();
            Result2.Text = X2.ToString();
            }
        }
    }
}

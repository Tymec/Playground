using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication6
{
    public partial class Form1 : Form
    {
        static Random NameGen = new Random((int)DateTime.Now.Ticks);
        public Form1()
        {
            InitializeComponent();
        }

        private void Generate_Click(object sender, EventArgs e)
        {
            FileStream fs = new FileStream(path, FileMode.OpenOrCreate);
            StreamWriter sw = new StreamWriter(fs);
            for (int i = 0; i < 100; i++)
            {
                string name = GetChar() + GetChar() + GetChar() + GetChar() + GetChar() + GetChar() + GetChar();
                Passwords.Items.Add(name);
                sw.WriteLine(name);
            }
            sw.Flush();
            fs.Close();
        }

        private string GetChar()
        {
            char c = (char)NameGen.Next(33, 126);
            return c.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SaveFileDialog location = new SaveFileDialog();
            location.Filter = "Text File | *.txt";
            location.DefaultExt = "txt";
            location.ShowDialog();
            path = location.FileName;

        }

        public string path { get; set; }

        private void Passwords_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void toolTip1_Popup(object sender, PopupEventArgs e)
        {

        }

        private void toolTip1_Popup_1(object sender, PopupEventArgs e)
        {

        }
    }
}

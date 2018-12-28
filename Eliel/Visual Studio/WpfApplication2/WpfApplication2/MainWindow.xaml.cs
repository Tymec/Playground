using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApplication2
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        List<Food> foodMemoryList = new List<Food>();
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "XML File | *.xml";
            if (ofd.ShowDialog() == true)
            {
                
                FileStream fs = new FileStream(ofd.FileName, FileMode.Open);
                StreamReader sr = new StreamReader(fs);
                string line = sr.ReadToEnd();

                while (!string.IsNullOrEmpty(line) && line.IndexOf("<food>") >= 0)
                {

                    Food food = new Food();
                    int foodStart = line.IndexOf("<food>");
                    int foodFinal = line.IndexOf("</food>") + 7;

                    int nameStart = line.IndexOf("<name>") + 6;
                    int nameFinal = line.IndexOf("</name>");

                    food.Name = line.Substring(nameStart, nameFinal - nameStart);

                    int priceStart = line.IndexOf("<price>") + 7;
                    int priceFinal = line.IndexOf("</price>");

                    food.Price = decimal.Parse(line.Substring(priceStart, priceFinal - priceStart).Remove(0, 1));

                    int descriptionStart = line.IndexOf("<description>") + 13;
                    int descriptionFinal = line.IndexOf("</description>");

                    food.Description = line.Substring(descriptionStart, descriptionFinal - descriptionStart);

                    int caloriesStart = line.IndexOf("<calories>") + 10;
                    int caloriesFinal = line.IndexOf("</calories>");

                    food.Calories = int.Parse(line.Substring(caloriesStart, caloriesFinal - caloriesStart));

                    line = line.Remove(foodStart, foodFinal - foodStart);

                    foodMemoryList.Add(food);
                }

                foodList.ItemsSource = foodMemoryList;

                sr.Close();
                fs.Close();


            }
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            var query = from Food food in foodMemoryList where food.Name.Contains("Waffles") select food;
            Waffles.ItemsSource = query.ToList();

            
        }

        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
            var query = from Food food in foodMemoryList where food.Name.Contains("Pizza") select food;
            Pizza.ItemsSource = query.ToList();
        }
    }
}
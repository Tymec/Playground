using System;
using System.Collections.Generic;
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
using WpfApplication3.CurrencyConverterNS;


namespace WpfApplication3
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Convert_Click(object sender, RoutedEventArgs e)
        {
            CurrencyConvertorSoapClient client = new CurrencyConvertorSoapClient("CurrencyConvertorSoap");

            double convertionRate = client.ConversionRate(Currency.USD, Currency.NOK);

            double USD = double.Parse(USDAmount.Text);

            NOKAmount.Text = (USD * convertionRate).ToString();





        }

        private void Convertfrom_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {

        }
    }
}

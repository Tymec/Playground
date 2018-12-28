using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using WebApplication1.NA1;

namespace WebApplication1
{
    public partial class WebForm2 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Calculate_Click(object sender, EventArgs e)
        {
            CurrencyConvertorSoapClient client = new CurrencyConvertorSoapClient("CurrencyConvertorSoap");

            double convertionRate = client.ConversionRate(Currency.USD, Currency.NOK);

            double dUSD = 0.0d;

            if(double.TryParse(USD.Text, out dUSD))
            {
                NOK.Text = (dUSD * convertionRate).ToString();
            }
            else
            {
                NOK.Text = "That's not a number!";
            }
        }
    }
}
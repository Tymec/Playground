using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication1
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            Literal1.Text= "There are " + Calendar2.SelectedDate.Subtract(Calendar1.SelectedDate).Days + " days between " + Calendar1.SelectedDate.ToShortDateString() + " and " + Calendar2.SelectedDate.ToShortDateString();
            Literal1.Text += "<br/>You are allowed to take until: " + Calendar1.SelectedDate.AddDays(25).ToShortDateString();

        }
    }
}
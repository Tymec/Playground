<%@ Page Title="" Language="C#" MasterPageFile="~/Site1.Master" AutoEventWireup="true" CodeBehind="WebForm2.aspx.cs" Inherits="WebApplication1.WebForm2" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <asp:Label ID="Label2" runat="server" Text="USD"></asp:Label>
    <asp:TextBox ID="USD" runat="server"></asp:TextBox>
    <asp:Label ID="Label1" runat="server" Text="NOK"></asp:Label>
    <asp:TextBox ID="NOK" runat="server" Enabled="false" ></asp:TextBox>
    <asp:Button ID="Calculate" runat="server" Text="Calculate" OnClick="Calculate_Click" />
    </asp:Content>

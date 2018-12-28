<%@ Page Title="" Language="C#" MasterPageFile="~/Site1.Master" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
    <title>Home Page</title>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <asp:Calendar ID="Calendar1" runat="server"></asp:Calendar>
    <asp:Literal ID="Literal1" runat="server" />
    <asp:Calendar ID="Calendar2" runat="server"></asp:Calendar>
    <asp:Button ID="Button1" runat="server" Text="Calcualte" Height="35px" OnClick="Button1_Click" Width="259px"/>
    </asp:Content>


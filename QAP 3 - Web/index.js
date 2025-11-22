// Desc: Lawncare service calculator for Mo's Lawncare Services
// Author: Nolan Butt
// Dates: 2025-11-19

// Define required libraries
var $ = function (id) {
  return document.getElementById(id);
};


// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});


// Define program constants.
const BORDER_PERCENT = 0.04;
const LAWN_PERCENT = 0.95;
const BORDER_RATE = 0.28;
const LAWN_RATE = 0.04;
const FERTILIZER_RATE = 0.03;
const HST_RATE = 0.15;
const ENVIRONMENTAL_TAX_RATE = 0.014;


// Start main program here.

// Gather user inputs.
let customername = prompt("Enter customer name: ");
let streetaddress = prompt("Enter street address: ");
let city = prompt("Enter city: ");
let phonenumber = prompt("Enter phone number (999-999-9999): ");
let propertysize = parseFloat(prompt("Enter property size (in square feet): "));


// Perform required calculations.
let bordersqft = propertysize * BORDER_PERCENT;
let bordercost = bordersqft * BORDER_RATE;

let lawnsqft = propertysize * LAWN_PERCENT;
let lawncost = lawnsqft * LAWN_RATE;

let fertilizercost = propertysize * FERTILIZER_RATE;

let totalcharges = bordercost + lawncost + fertilizercost;

let salestax = totalcharges * HST_RATE;
let environmentaltax = totalcharges * ENVIRONMENTAL_TAX_RATE;

let invoicetotal = totalcharges + salestax + environmentaltax;


// Display results
document.writeln("<br />");
document.writeln("<table class='lawntable'>");

document.writeln("<tr class = yellowback>");
document.writeln("<td colspan='3' height='70px' class=boldtext >Mo's Lawncare Services - Customer Invoice</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan='3'>Customer Details:<br />" + "<center><br />" + customername + "<br />" + streetaddress + "<br />" + city + " " + phonenumber + "<br /></center><br />Property Size (in sq ft): " + " " + com2Format.format(propertysize) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Border cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(bordercost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Mowing cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(lawncost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Fertilizer cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(fertilizercost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='whiteback'>&nbsp;</td>");
document.writeln("<td class='whiteback'>&nbsp;</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Total charges:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(totalcharges) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='whiteback'>&nbsp;</td>");
document.writeln("<td class='whiteback'>&nbsp;</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Sales tax (HST):</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(salestax) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Environmental tax:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(environmentaltax) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class='whiteback'>&nbsp;</td>");
document.writeln("<td class='whiteback'>&nbsp;</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Invoice total:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(invoicetotal) + "</td>");
document.writeln("</tr>");

document.writeln("<tr class = yellowback>");
document.writeln("<td colspan='3' height='70px' class=boldtext >Turning Lawns into Landscapes</td>");
document.writeln("</tr>");

document.writeln("</table>");


json = {
  "shipmentReference": "SR12345",
  "shipmentControlNumber": "SCN67890",
  "exporterSeller": {
    "name": "ABC Exporters Inc.",
    "address": "123 Main St, New York, NY 10001",
    "contact": "John Doe (212) 555-1234"
  },
  "producerOfGoods": {
    "name": "XYZ Manufacturers Ltd.",
    "address": "456 Industrial Ave, Chicago, IL 60606",
    "contact": "Jane Smith (312) 555-5678"
  },
  "shippedToConsignee": {
    "name": "DEF Importers Corp.",
    "address": "789 Broadway, Los Angeles, CA 90012",
    "contact": "Bob Johnson (213) 555-9012"
  },
  "buyer": {
    "name": "GHI Trading Co.",
    "address": "321 Market St, San Francisco, CA 94105",
    "contact": "Alice Brown (415) 555-1111"
  },
  "irsNumbers": {
    "exporter": "123456789",
    "consignee": "987654321"
  },
  "relationshipBetweenParties": "NOT RELATED",
  "countryOfFinalDestination": "USA",
  "invoiceDate": "2023-09-20",
  "dateOfSale": "2023-09-15",
  "usDutyBrokerageAccount": "EXPORTER",
  "shipToConsigneeOther": "",
  "livingstonAccountNumber": "LA12345",
  "discounts": "",
  "portOfEntry": "Los Angeles",
  "termsOfSale": "FOB",
  "marksAndNumbers": "Container 1 of 2",
  "packages": [
    {
      "number": "1",
      "kind": "Box",
      "shippingWeight": "100 lbs",
      "freightAmountIncluded": "$500.00",
      "freightAmountToBorder": "$200.00",
      "countryOfOrigin": "USA",
      "descriptionOfGoods": "Electronics",
      "htsNumber": "85437099",
      "unitQuantity": "50",
      "unitPrice": "$100.00",
      "invoiceTotal": "$5000.00"
    },
    {
      "number": "2",
      "kind": "Pallet",
      "shippingWeight": "500 lbs",
      "freightAmountIncluded": "$2000.00",
      "freightAmountToBorder": "$800.00",
      "countryOfOrigin": "Canada",
      "descriptionOfGoods": "Textiles",
      "htsNumber": "62034210",
      "unitQuantity": "100",
      "unitPrice": "$50.00",
      "invoiceTotal": "$5000.00"
    }
  ],
  "foodImport": {
    "refusedByOtherCountries": "No",
    "productsRefused": "",
    "countriesThatRefused": ""
  },
  "invoiceTotal": "$10000.00",
  "pricesInclude": ["DUTY", "BROKERAGE", "FREIGHT"],
  "declarationByForeignShipper": {
    "usOrigin": False,
    "portOfExport": "",
    "exportDate": "",
    "returnedWithoutImprovement": False,
    "manufacturerAffidavitAttached": False,
    "signature": "",
    "dateSigned": ""
  },
  "preparerDetails": {
    "isExporter": True,
    "name": "John Doe",
    "employeeTitle": "Shipping Manager"
  },
  "currencyOfSale": "USD",
  "comments": "Special care required for electronics package."
}

shipmentKeyMap = {
  "Shipment Reference Number": "shipmentReference",
  "Shipment Control Number": "shipmentControlNumber",
  
  "Name of the exporting seller": "exporterSeller.name",
  "Address of the exporting seller": "exporterSeller.address",
  "Contact information of the exporting seller": "exporterSeller.contact",
  
  "Name of the producer of goods": "producerOfGoods.name",
  "Address of the producer of goods": "producerOfGoods.address",
  "Contact information of the producer of goods": "producerOfGoods.contact",
  
  "Name of the consignee shipping to": "shippedToConsignee.name",
  "Address of the consignee shipping to": "shippedToConsignee.address",
  "Contact information of the consignee shipping to": "shippedToConsignee.contact",
  
  "Name of the buyer": "buyer.name",
  "Address of the buyer": "buyer.address",
  "Contact information of the buyer": "buyer.contact",
  
  "IRS number of the exporter": "irsNumbers.exporter",
  "IRS number of the consignee": "irsNumbers.consignee",
  
  "Relationship between parties": "relationshipBetweenParties",
  "Country of final destination": "countryOfFinalDestination",
  "Invoice date": "invoiceDate",
  "Date of sale": "dateOfSale",
  "US duty brokerage account": "usDutyBrokerageAccount",
  "Additional shipping instructions for consignee": "shipToConsigneeOther",
  "Livingston account number": "livingstonAccountNumber",
  "Discounts applied": "discounts",
  "Port of entry": "portOfEntry",
  "Terms of sale": "termsOfSale",
  "Marks and numbers on packages": "marksAndNumbers",
  
  "Package number": "packages.0.number",
  "Type of package": "packages.0.kind",
  "Shipping weight of package": "packages.0.shippingWeight",
  "Freight amount included": "packages.0.freightAmountIncluded",
  "Freight amount to border": "packages.0.freightAmountToBorder",
  "Country of origin of goods": "packages.0.countryOfOrigin",
  "Description of goods": "packages.0.descriptionOfGoods",
  "HTS number": "packages.0.htsNumber",
  "Unit quantity": "packages.0.unitQuantity",
  "Unit price": "packages.0.unitPrice",
  "Invoice total for package": "packages.0.invoiceTotal",
  
  "Has product been refused by other countries?": "foodImport.refusedByOtherCountries",
  "Products refused": "foodImport.productsRefused",
  "Countries that refused products": "foodImport.countriesThatRefused",
  
  "Total invoice amount": "invoiceTotal",
  "Prices include": "pricesInclude",
  
  "Is US origin?": "declarationByForeignShipper.usOrigin",
  "Port of export": "declarationByForeignShipper.portOfExport",
  "Export date": "declarationByForeignShipper.exportDate",
  "Returned without improvement?": "declarationByForeignShipper.returnedWithoutImprovement",
  "Manufacturer affidavit attached?": "declarationByForeignShipper.manufacturerAffidavitAttached",
  "Signature": "declarationByForeignShipper.signature",
  "Date signed": "declarationByForeignShipper.dateSigned",
  
  "Is preparer the exporter?": "preparerDetails.isExporter",
  "Preparer's name": "preparerDetails.name",
  "Preparer's employee title": "preparerDetails.employeeTitle",
  
  "Currency of sale": "currencyOfSale",
  "Comments": "comments"
};

english_keys = sorted(shipmentKeyMap.keys())

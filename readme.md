# Overview
Crypto-Notifier is a program designed to monitor cryptocurrency prices and notify users about significant changes. It provides functionalities such as tracking crypto balances, setting notification thresholds, and detecting price peaks or drops.

Author: Thomas Vernoux
Date: March 2024

# Program Description

## Actions

The program performs the following tasks:

### Crypto Price Update
Using the Coinbase API, the program updates the prices of cryptocurrencies.

### Crypto Account Update
Using the Coinbase API, the program updates the cryptocurrency accounts.

### Peak Detection and Selling
The program detects when the price of a cryptocurrency reaches a peak and sells the cryptocurrency if necessary.

### Storing Crypto Prices
The program stores cryptocurrency prices in a SQL database.

# Installation

## Requirements
The required libraries are listed in the requirements file.

## Compatibility
This code works with the Coinbase API: https://www.coinbase.com/

## Access
An API key file is required. Get an API key from Coinbase and place it in the api_keys directory.

# Documentation

Advanced Trade API welcome: https://docs.cloud.coinbase.com/advanced-trade-api/docs/welcome
Advanced Trade API documentation: https://coinbase.github.io/coinbase-advanced-py

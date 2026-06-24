# Data Dictionary

## 02_nav_history_cleaned.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Mutual fund identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## 08_investor_transactions_cleaned.csv

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | Integer | Investor identifier |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Fund identifier |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction amount |
| state | Text | Investor state |
| kyc_status | Text | KYC verification status |

---

## 07_scheme_performance_cleaned.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Fund identifier |
| scheme_name | Text | Scheme name |
| return_1yr_pct | Float | One-year return |
| return_3yr_pct | Float | Three-year return |
| return_5yr_pct | Float | Five-year return |
| alpha | Float | Risk-adjusted return metric |
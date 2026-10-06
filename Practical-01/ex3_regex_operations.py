import re

text = """
Log:
- Alice: alice@work.com, Phone: 555-0199
- Bob: bad-email@domain, Phone: 555-0200
"""

# ---------- 1. SEARCH: extract valid emails ----------
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
print("Valid Emails:", emails)

# ---------- 2. SEARCH: extract phone numbers ----------
phones = re.findall(r"\b\d{3}-\d{4}\b", text)
print("Phone Numbers:", phones)

# ---------- 3. SPLIT: tokenize a delimited line ----------
line = "Item1; 29.99 | InStock , Category-A"
print("Tokens:", [t.strip() for t in re.split(r"[;,|]", line)])

# ---------- 4. REPLACE: mask email usernames ----------
masked = re.sub(
    r"\b([A-Za-z0-9._%+-]+)(@[A-Za-z0-9.-]+\.[A-Za-z]{2,})\b",
    r"****\2",
    text,
)
print("\nMasked Log:\n", masked)

# ---------- 5. MATCH: check first line for a keyword ----------
first_match = re.search(r"Log", text)
if first_match:
    print("\nPattern 'Log' found at position:", first_match.start())
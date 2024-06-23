import ldap

LDAP_SERVER = "ldaps://ldap.google.com"
# BIND_DN = "cn=admin,dc=example,dc=com" 
BIND_DN = "uid=admin,ou=system"
BIND_PASSWORD = "password"  

# Bỏ qua kiểm tra chứng chỉ (cho phát triển)
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

try:
    conn = ldap.initialize(LDAP_SERVER)
    conn.simple_bind_s(BIND_DN, BIND_PASSWORD)
    print("Successfully connected to LDAP server")
except ldap.LDAPError as e:
    print(f"Failed to connect to LDAP server: {e}")

from OpenSSL import crypto
import pem

def verify(cert_file_name, int_cert_file_name, title):
    with open(cert_file_name, 'r') as cert_file:
        cert = cert_file.read()
    with open(int_cert_file_name, 'r') as int_cert_file:
        int_cert = int_cert_file.read()
    pems = pem.parse_file('./ca-certificates.crt')
    trusted_certs = []
    for mypem in pems:
        trusted_certs.append(str(mypem))
    trusted_certs.append(int_cert)
    verified = verify_chain_of_trust(cert, trusted_certs)
    if verified:
        print(f'✅ {title} certificate verified')

def verify_chain_of_trust(cert_pem, trusted_cert_pems):
    certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)
    # Create and fill a X509Store with trusted certs
    store = crypto.X509Store()
    for trusted_cert_pem in trusted_cert_pems:
        trusted_cert = crypto.load_certificate(crypto.FILETYPE_PEM,
                                             trusted_cert_pem)
        store.add_cert(trusted_cert)
    # Create a X590StoreContext with the cert and trusted certs
    # and verify the the chain of trust
    store_ctx = crypto.X509StoreContext(store, certificate)
    # Returns None if certificate can be validated
    result = store_ctx.verify_certificate()
    if result is None:
        return True
    else:
        return False

verify('twitter.cert', 'twitter_intermediate.cert', 'twitter')
verify('google.cert', 'google_intermediate.cert', 'google')
verify('chula.cert', 'chula_intermediate.cert', 'chula')
verify('classdeedee.cert', 'classdeedee_intermediate.cert', 'classdeedee')
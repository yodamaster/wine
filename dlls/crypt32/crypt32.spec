name crypt32
type win32

import advapi32.dll
import kernel32.dll
import ntdll.dll

debug_channels ()

@ stub CertAddCRLContextToStore
@ stub CertAddCTLContextToStore
@ stub CertAddCertificateContextToStore
@ stub CertAddEncodedCRLToStore
@ stub CertAddEncodedCTLToStore
@ stub CertAddEncodedCertificateToStore
@ stub CertAddEncodedCertificateToSystemStoreA
@ stub CertAddEncodedCertificateToSystemStoreW
@ stub CertAddEnhancedKeyUsageIdentifier
@ stub CertAddSerializedElementToStore
@ stub CertAddStoreToCollection
@ stub CertAlgIdToOID
@ stub CertCloseStore
@ stub CertCompareCertificate
@ stub CertCompareCertificateName
@ stub CertCompareIntegerBlob
@ stub CertComparePublicKeyInfo
@ stub CertControlStore
@ stub CertCreateCRLContext
@ stub CertCreateCTLContext
@ stub CertCreateCertificateChainEngine
@ stub CertCreateCertificateContext
@ stub CertDeleteCRLFromStore
@ stub CertDeleteCTLFromStore
@ stub CertDeleteCertificateFromStore
@ stub CertDuplicateCRLContext
@ stub CertDuplicateCTLContext
@ stub CertDuplicateCertificateContext
@ stub CertDuplicateStore
@ stub CertEnumCRLContextProperties
@ stub CertEnumCTLContextProperties
@ stub CertEnumCTLsInStore
@ stub CertEnumCertificateContextProperties
@ stub CertEnumCertificatesInStore
@ stub CertFindAttribute
@ stub CertFindCTLInStore
@ stub CertFindCertificateInStore
@ stub CertFindExtension
@ stub CertFindRDNAttr
@ stub CertFindSubjectInCTL
@ stub CertFreeCRLContext
@ stub CertFreeCTLContext
@ stub CertFreeCertificateChain
@ stub CertFreeCertificateChainEngine
@ stub CertFreeCertificateContext
@ stub CertGetCRLContextProperty
@ stub CertGetCRLFromStore
@ stub CertGetCTLContextProperty
@ stub CertGetCertificateContextProperty
@ stub CertGetEnhancedKeyUsage
@ stub CertGetIntendedKeyUsage
@ stub CertGetIssuerCertificateFromStore
@ stub CertGetPublicKeyLength
@ stub CertGetCertificateChain
@ stub CertGetSubjectCertificateFromStore
@ stub CertIsRDNAttrsInCertificateName
@ stub CertNameToStrA
@ stub CertNameToStrW
@ stub CertOIDToAlgId
@ stub CertOpenStore
@ stub CertOpenSystemStoreA
@ stub CertOpenSystemStoreW
@ stub CertRDNValueToStrA
@ stub CertRDNValueToStrW
@ stub CertRemoveEnhancedKeyUsageIdentifier
@ stub CertSaveStore
@ stub CertSerializeCRLStoreElement
@ stub CertSerializeCTLStoreElement
@ stub CertSerializeCertificateStoreElement
@ stub CertSetCRLContextProperty
@ stub CertSetCTLContextProperty
@ stub CertSetCertificateContextProperty
@ stub CertSetEnhancedKeyUsage
@ stub CertStrToNameA
@ stub CertStrToNameW
@ stub CertVerifyCRLRevocation
@ stub CertVerifyCRLTimeValidity
@ stub CertVerifyCTLUsage
@ stub CertVerifyRevocation
@ stub CertVerifySubjectCertificateContext
@ stub CertVerifyTimeValidity
@ stub CertVerifyValidityNesting
@ stub CreateFileU
@ stub CryptAcquireContextU
@ stub CryptCloseAsyncHandle
@ stub CryptCreateAsyncHandle
@ stub CryptDecodeMessage
@ stub CryptDecodeObject
@ stub CryptDecryptAndVerifyMessageSignature
@ stub CryptDecryptMessage
@ stub CryptEncodeObject
@ stub CryptEncryptMessage
@ stub CryptEnumOIDFunction
@ stub CryptEnumOIDInfo
@ stub CryptEnumProvidersU
@ stub CryptExportPKCS8
@ stub CryptExportPublicKeyInfo
@ stub CryptExportPublicKeyInfoEx
@ stub CryptFindOIDInfo
@ stub CryptFormatObject
@ stub CryptFreeOIDFunctionAddress
@ stub CryptGetAsyncParam
@ stub CryptGetDefaultOIDDllList
@ stub CryptGetDefaultOIDFunctionAddress
@ stub CryptGetMessageCertificates
@ stub CryptGetMessageSignerCount
@ stub CryptGetOIDFunctionAddress
@ stub CryptGetOIDFunctionValue
@ stub CryptHashCertificate
@ stub CryptHashMessage
@ stub CryptHashPublicKeyInfo
@ stub CryptHashToBeSigned
@ stub CryptImportPKCS8
@ stub CryptImportPublicKeyInfo
@ stub CryptImportPublicKeyInfoEx
@ stub CryptInitOIDFunctionSet
@ stub CryptInstallOIDFunctionAddress
@ stub CryptLoadSip
@ stub CryptMemAlloc
@ stub CryptMemFree
@ stub CryptMemRealloc
@ stub CryptMsgCalculateEncodedLength
@ stub CryptMsgClose
@ stub CryptMsgControl
@ stub CryptMsgCountersign
@ stub CryptMsgCountersignEncoded
@ stub CryptMsgEncodeAndSignCTL
@ stub CryptMsgGetAndVerifySigner
@ stub CryptMsgGetParam
@ stub CryptMsgOpenToDecode
@ stub CryptMsgOpenToEncode
@ stub CryptMsgSignCTL
@ stub CryptMsgUpdate
@ stub CryptMsgVerifyCountersignatureEncoded
@ stub CryptRegisterDefaultOIDFunction
@ stub CryptRegisterOIDFunction
@ stub CryptRegisterOIDInfo
@ stub CryptSIPAddProvider
@ stub CryptSIPLoad
@ stub CryptSIPRemoveProvider
@ stub CryptSIPRetrieveSubjectGuid
@ stub CryptSetAsyncParam
@ stub CryptSetOIDFunctionValue
@ stub CryptSetProviderU
@ stub CryptSignAndEncodeCertificate
@ stub CryptSignAndEncryptMessage
@ stub CryptSignCertificate
@ stub CryptSignHashU
@ stub CryptSignMessage
@ stub CryptSignMessageWithKey
@ stub CryptUnregisterDefaultOIDFunction
@ stub CryptUnregisterOIDFunction
@ stub CryptUnregisterOIDInfo
@ stub CryptVerifyCertificateSignature
@ stub CryptVerifyDetachedMessageHash
@ stub CryptVerifyDetachedMessageSignature
@ stub CryptVerifyMessageHash
@ stub CryptVerifyMessageSignature
@ stub CryptVerifyMessageSignatureWithKey
@ stub CryptVerifySignatureU
@ stub I_CryptAllocTls
@ stdcall I_CryptCreateLruCache(long long) I_CryptCreateLruCache
@ stub I_CryptCreateLruEntry
@ stub I_CryptDetachTls
@ stdcall I_CryptFindLruEntryData(long) I_CryptFindLruEntryData
@ stdcall I_CryptFlushLruCache(long) I_CryptFlushLruCache
@ stdcall I_CryptFreeLruCache(long) I_CryptFreeLruCache
@ stub I_CryptGetDefaultCryptProv
@ stub I_CryptGetDefaultCryptProvForEncrypt
@ stub I_CryptGetOssGlobal
@ stub I_CryptGetTls
@ stub I_CryptInsertLruEntry
@ stub I_CryptInstallOssGlobal
@ stub I_CryptReleaseLruEntry
@ stub I_CryptSetTls
@ stub I_CryptUninstallOssGlobal
@ stub PFXExportCertStore
@ stub PFXImportCertStore
@ stub RegCreateHKCUKeyExU
@ stub RegCreateKeyExU
@ stub RegDeleteValueU
@ stub RegEnumValueU
@ stub RegOpenHKCUKeyExU
@ stub RegOpenKeyExU
@ stub RegQueryInfoKeyU
@ stub RegQueryValueExU
@ stub RegSetValueExU

# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::NotificationHubs
  module Models
    #
    # Description of a NotificationHub MpnsCredential.
    #
    class MpnsCredentialProperties

      include MsRestAzure

      # @return [String] Gets or sets the MPNS certificate.
      attr_accessor :mpns_certificate

      # @return [String] Gets or sets the certificate key for this credential.
      attr_accessor :certificate_key

      # @return [String] Gets or sets the Mpns certificate Thumbprint
      attr_accessor :thumbprint


      #
      # Mapper for MpnsCredentialProperties class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'MpnsCredentialProperties',
          type: {
            name: 'Composite',
            class_name: 'MpnsCredentialProperties',
            model_properties: {
              mpns_certificate: {
                required: false,
                serialized_name: 'mpnsCertificate',
                type: {
                  name: 'String'
                }
              },
              certificate_key: {
                required: false,
                serialized_name: 'certificateKey',
                type: {
                  name: 'String'
                }
              },
              thumbprint: {
                required: false,
                serialized_name: 'thumbprint',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end
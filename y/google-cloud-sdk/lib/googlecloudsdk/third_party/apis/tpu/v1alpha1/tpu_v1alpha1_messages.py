"""Generated message classes for tpu version v1alpha1.

TPU API provides customers with access to Google TPU technology.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'tpu'


class AcceleratorType(_messages.Message):
  r"""A accelerator type that a Node can be configured with.

  Fields:
    name: The resource name.
    type: the accelerator type.
  """

  name = _messages.StringField(1)
  type = _messages.StringField(2)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class ListAcceleratorTypesResponse(_messages.Message):
  r"""Response for ListAcceleratorTypes.

  Fields:
    acceleratorTypes: The listed nodes.
    nextPageToken: The next page token or empty if none.
  """

  acceleratorTypes = _messages.MessageField('AcceleratorType', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListNodesResponse(_messages.Message):
  r"""Response for ListNodes.

  Fields:
    nextPageToken: The next page token or empty if none.
    nodes: The listed nodes.
    unreachable: Locations that could not be reached.
  """

  nextPageToken = _messages.StringField(1)
  nodes = _messages.MessageField('Node', 2, repeated=True)
  unreachable = _messages.StringField(3, repeated=True)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class ListTensorFlowVersionsResponse(_messages.Message):
  r"""Response for ListTensorFlowVersions.

  Fields:
    nextPageToken: The next page token or empty if none.
    tensorflowVersions: The listed nodes.
  """

  nextPageToken = _messages.StringField(1)
  tensorflowVersions = _messages.MessageField('TensorFlowVersion', 2, repeated=True)


class Location(_messages.Message):
  r"""A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class NetworkEndpoint(_messages.Message):
  r"""A network endpoint over which a TPU worker can be reached.

  Fields:
    ipAddress: The IP address of this network endpoint.
    port: The port of this network endpoint.
  """

  ipAddress = _messages.StringField(1)
  port = _messages.IntegerField(2, variant=_messages.Variant.INT32)


class Node(_messages.Message):
  r"""A TPU instance.

  Enums:
    HealthValueValuesEnum: The health status of the TPU node.
    StateValueValuesEnum: Output only. The current state for the TPU Node.

  Messages:
    LabelsValue: Resource labels to represent user-provided metadata.

  Fields:
    acceleratorType: The type of hardware accelerators associated with this
      node. Required.
    cidrBlock: The CIDR block that the TPU node will use when selecting an IP
      address. This CIDR block must be a /29 block; the Compute Engine
      networks API forbids a smaller block, and using a larger block would be
      wasteful (a node can only consume one IP address). Errors will occur if
      the CIDR block has already been used for a currently existing TPU node,
      the CIDR block conflicts with any subnetworks in the user's provided
      network, or the provided network is peered with another network that is
      using that CIDR block. Required.
    createTime: Output only. The time when the node was created.
    description: The user-supplied description of the TPU. Maximum of 512
      characters.
    health: The health status of the TPU node.
    healthDescription: Output only. If this field is populated, it contains a
      description of why the TPU Node is unhealthy.
    ipAddress: Output only. DEPRECATED! Use network_endpoints instead. The
      network address for the TPU Node as visible to Compute Engine instances.
    labels: Resource labels to represent user-provided metadata.
    name: Output only. The immutable name of the TPU
    network: The name of a network they wish to peer the TPU node to. It must
      be a preexisting Compute Engine network inside of the project on which
      this API has been activated. If none is provided, "default" will be
      used.
    networkEndpoints: Output only. The network endpoints where TPU workers can
      be accessed and sent work. It is recommended that Tensorflow clients of
      the node reach out to the 0th entry in this map first.
    port: Output only. DEPRECATED! Use network_endpoints instead. The network
      port for the TPU Node as visible to Compute Engine instances.
    schedulingConfig: A SchedulingConfig attribute.
    serviceAccount: Output only. The service account used to run the tensor
      flow services within the node. To share resources, including Google
      Cloud Storage data, with the Tensorflow job running in the Node, this
      account must have permissions to that data.
    state: Output only. The current state for the TPU Node.
    tensorflowVersion: The version of Tensorflow running in the Node.
      Required.
    useServiceNetworking: Whether the VPC peering for the node is set up
      through Service Networking API. The VPC Peering should be set up before
      provisioning the node. If this field is set, cidr_block field should not
      be specified. If the network, that you want to peer the TPU Node to, is
      Shared VPC networks, the node must be created with this this field
      enabled.
  """

  class HealthValueValuesEnum(_messages.Enum):
    r"""The health status of the TPU node.

    Values:
      HEALTH_UNSPECIFIED: Health status is unknown: not initialized or failed
        to retrieve.
      HEALTHY: The resource is healthy.
      UNHEALTHY: The resource is unhealthy.
      TIMEOUT: The resource is unresponsive.
    """
    HEALTH_UNSPECIFIED = 0
    HEALTHY = 1
    UNHEALTHY = 2
    TIMEOUT = 3

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. The current state for the TPU Node.

    Values:
      STATE_UNSPECIFIED: TPU node state is not known/set.
      CREATING: TPU node is being created.
      READY: TPU node has been created and is fully usable.
      RESTARTING: TPU node is restarting.
      REIMAGING: TPU node is undergoing reimaging.
      DELETING: TPU node is being deleted.
      REPAIRING: TPU node is being repaired and may be unusable. Details can
        be found in the `help_description` field.
      STOPPED: 7 - Reserved. Was SUSPENDED. TPU node is stopped.
      STOPPING: TPU node is currently stopping.
      STARTING: TPU node is currently starting.
      PREEMPTED: TPU node has been preempted. Only applies to Preemptible TPU
        Nodes.
      TERMINATED: TPU node has been terminated due to maintenance or has
        reached the end of its life cycle (for preemptible nodes).
    """
    STATE_UNSPECIFIED = 0
    CREATING = 1
    READY = 2
    RESTARTING = 3
    REIMAGING = 4
    DELETING = 5
    REPAIRING = 6
    STOPPED = 7
    STOPPING = 8
    STARTING = 9
    PREEMPTED = 10
    TERMINATED = 11

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Resource labels to represent user-provided metadata.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  acceleratorType = _messages.StringField(1)
  cidrBlock = _messages.StringField(2)
  createTime = _messages.StringField(3)
  description = _messages.StringField(4)
  health = _messages.EnumField('HealthValueValuesEnum', 5)
  healthDescription = _messages.StringField(6)
  ipAddress = _messages.StringField(7)
  labels = _messages.MessageField('LabelsValue', 8)
  name = _messages.StringField(9)
  network = _messages.StringField(10)
  networkEndpoints = _messages.MessageField('NetworkEndpoint', 11, repeated=True)
  port = _messages.StringField(12)
  schedulingConfig = _messages.MessageField('SchedulingConfig', 13)
  serviceAccount = _messages.StringField(14)
  state = _messages.EnumField('StateValueValuesEnum', 15)
  tensorflowVersion = _messages.StringField(16)
  useServiceNetworking = _messages.BooleanField(17)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should have the format of `operations/some/unique/name`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OperationMetadata(_messages.Message):
  r"""Represents the metadata of the long-running operation.

  Fields:
    apiVersion: [Output only] API version used to start the operation.
    cancelRequested: [Output only] Identifies whether the user has requested
      cancellation of the operation. Operations that have successfully been
      cancelled have Operation.error value with a google.rpc.Status.code of 1,
      corresponding to `Code.CANCELLED`.
    createTime: [Output only] The time the operation was created.
    endTime: [Output only] The time the operation finished running.
    statusDetail: [Output only] Human-readable status of the operation, if
      any.
    target: [Output only] Server-defined resource path for the target of the
      operation.
    verb: [Output only] Name of the verb executed by the operation.
  """

  apiVersion = _messages.StringField(1)
  cancelRequested = _messages.BooleanField(2)
  createTime = _messages.StringField(3)
  endTime = _messages.StringField(4)
  statusDetail = _messages.StringField(5)
  target = _messages.StringField(6)
  verb = _messages.StringField(7)


class ReimageNodeRequest(_messages.Message):
  r"""Request for ReimageNode.

  Fields:
    tensorflowVersion: The version for reimage to create.
  """

  tensorflowVersion = _messages.StringField(1)


class SchedulingConfig(_messages.Message):
  r"""A SchedulingConfig object.

  Fields:
    preemptible: A boolean attribute.
    reserved: Whether the node is created under a reservation.
  """

  preemptible = _messages.BooleanField(1)
  reserved = _messages.BooleanField(2)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class StartNodeRequest(_messages.Message):
  r"""Request for StartNode."""


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` that can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting.  - Batch operations. If a
  client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class StopNodeRequest(_messages.Message):
  r"""Request for StopNode."""


class TensorFlowVersion(_messages.Message):
  r"""A tensorflow version that a Node can be configured with.

  Fields:
    name: The resource name.
    version: the tensorflow version.
  """

  name = _messages.StringField(1)
  version = _messages.StringField(2)


class TpuProjectsLocationsAcceleratorTypesGetRequest(_messages.Message):
  r"""A TpuProjectsLocationsAcceleratorTypesGetRequest object.

  Fields:
    name: The resource name.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsAcceleratorTypesListRequest(_messages.Message):
  r"""A TpuProjectsLocationsAcceleratorTypesListRequest object.

  Fields:
    filter: List filter.
    orderBy: Sort results.
    pageSize: The maximum number of items to return.
    pageToken: The next_page_token value returned from a previous List
      request, if any.
    parent: The parent resource name.
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


class TpuProjectsLocationsGetRequest(_messages.Message):
  r"""A TpuProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsListRequest(_messages.Message):
  r"""A TpuProjectsLocationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The resource that owns the locations collection, if applicable.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class TpuProjectsLocationsNodesCreateRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesCreateRequest object.

  Fields:
    node: A Node resource to be passed as the request body.
    nodeId: The unqualified resource name.
    parent: The parent resource name.
  """

  node = _messages.MessageField('Node', 1)
  nodeId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class TpuProjectsLocationsNodesDeleteRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesDeleteRequest object.

  Fields:
    name: The resource name.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsNodesGetRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesGetRequest object.

  Fields:
    name: The resource name.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsNodesListRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesListRequest object.

  Fields:
    pageSize: The maximum number of items to return.
    pageToken: The next_page_token value returned from a previous List
      request, if any.
    parent: The parent resource name.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class TpuProjectsLocationsNodesReimageRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesReimageRequest object.

  Fields:
    name: The resource name.
    reimageNodeRequest: A ReimageNodeRequest resource to be passed as the
      request body.
  """

  name = _messages.StringField(1, required=True)
  reimageNodeRequest = _messages.MessageField('ReimageNodeRequest', 2)


class TpuProjectsLocationsNodesStartRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesStartRequest object.

  Fields:
    name: The resource name.
    startNodeRequest: A StartNodeRequest resource to be passed as the request
      body.
  """

  name = _messages.StringField(1, required=True)
  startNodeRequest = _messages.MessageField('StartNodeRequest', 2)


class TpuProjectsLocationsNodesStopRequest(_messages.Message):
  r"""A TpuProjectsLocationsNodesStopRequest object.

  Fields:
    name: The resource name.
    stopNodeRequest: A StopNodeRequest resource to be passed as the request
      body.
  """

  name = _messages.StringField(1, required=True)
  stopNodeRequest = _messages.MessageField('StopNodeRequest', 2)


class TpuProjectsLocationsOperationsCancelRequest(_messages.Message):
  r"""A TpuProjectsLocationsOperationsCancelRequest object.

  Fields:
    name: The name of the operation resource to be cancelled.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsOperationsDeleteRequest(_messages.Message):
  r"""A TpuProjectsLocationsOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A TpuProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsOperationsListRequest(_messages.Message):
  r"""A TpuProjectsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class TpuProjectsLocationsTensorflowVersionsGetRequest(_messages.Message):
  r"""A TpuProjectsLocationsTensorflowVersionsGetRequest object.

  Fields:
    name: The resource name.
  """

  name = _messages.StringField(1, required=True)


class TpuProjectsLocationsTensorflowVersionsListRequest(_messages.Message):
  r"""A TpuProjectsLocationsTensorflowVersionsListRequest object.

  Fields:
    filter: List filter.
    orderBy: Sort results.
    pageSize: The maximum number of items to return.
    pageToken: The next_page_token value returned from a previous List
      request, if any.
    parent: The parent resource name.
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')

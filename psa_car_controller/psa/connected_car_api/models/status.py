# coding: utf-8

"""
    Groupe PSA Connected Car - WEB API B2C

    *PSA B2C Connected Car API*  # Introduction This is the description of the *Groupe PSA Connected Car V2 API*. The speccification is  is based on **OpenAPI Specification version 3** and can be displayed via [ReDoc](https://github.com/Rebilly/ReDoc)a or [Swagger](http://swagger.io).   This API allows applications to fetch data from the connected Vehicles data platform. # Authentication PSA Connected Car APIs uses the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for authentication and Authorization. any application require a valid [Access Token](https://tools.ietf.org/html/rfc6749#section-1.4) to access to user data. # Errors   Error codes returned by all REST APIs comply with the standard. Nevertheless, PSA Services (callers) need to have more complete data structures (even when the answer is not Http-OK) to better detail the type of error by providing application code, message and a debugging code(for investigation purposes). The http code of the response is managed by the protocol itself (in the header).      **Errors are  returned as a generic error response:**    * ```xError``` object model.       # noqa: E501

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Status(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'embedded': 'StatusEmbedded',
        'links': 'StatusLinks',
        'battery': 'Battery',
        'doors_state': 'DoorsState',
        'energy': 'list[Energy]',
        'environment': 'Environment',
        'ignition': 'Ignition',
        'kinetic': 'Kinetic',
        'last_position': 'Position',
        'preconditionning': 'Preconditioning',
        'privacy': 'Privacy',
        'safety': 'Safety',
        'service': 'ServiceType',
        'timed_odometer': 'VehicleOdometer'
    }

    attribute_map = {
        'embedded': '_embedded',
        'links': '_links',
        'battery': 'battery',
        'doors_state': 'doorsState',
        'energy': 'energy',
        'environment': 'environment',
        'ignition': 'ignition',
        'kinetic': 'kinetic',
        'last_position': 'lastPosition',
        'preconditionning': 'preconditionning',
        'privacy': 'privacy',
        'safety': 'safety',
        'service': 'service',
        'timed_odometer': 'odometer'
    }

    def __init__(self, embedded=None, links=None, battery=None, doors_state=None, energy=None, environment=None, ignition=None, kinetic=None, last_position=None, preconditionning=None, privacy=None, safety=None, service=None, timed_odometer=None):  # noqa: E501
        """Status - a model defined in Swagger"""  # noqa: E501

        self._embedded = None
        self._links = None
        self._battery = None
        self._doors_state = None
        self._energy = None
        self._environment = None
        self._ignition = None
        self._kinetic = None
        self._last_position = None
        self._preconditionning = None
        self._privacy = None
        self._safety = None
        self._service = None
        self._timed_odometer = None
        self.discriminator = None

        if embedded is not None:
            self.embedded = embedded
        self.links = links
        if battery is not None:
            self.battery = battery
        if doors_state is not None:
            self.doors_state = doors_state
        if energy is not None:
            self.energy = energy
        if environment is not None:
            self.environment = environment
        if ignition is not None:
            self.ignition = ignition
        if kinetic is not None:
            self.kinetic = kinetic
        if last_position is not None:
            self.last_position = last_position
        if preconditionning is not None:
            self.preconditionning = preconditionning
        if privacy is not None:
            self.privacy = privacy
        if safety is not None:
            self.safety = safety
        if service is not None:
            self.service = service
        if timed_odometer is not None:
            self.timed_odometer = timed_odometer

    @property
    def embedded(self):
        """Gets the embedded of this Status.  # noqa: E501


        :return: The embedded of this Status.  # noqa: E501
        :rtype: StatusEmbedded
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this Status.


        :param embedded: The embedded of this Status.  # noqa: E501
        :type: StatusEmbedded
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this Status.  # noqa: E501


        :return: The links of this Status.  # noqa: E501
        :rtype: StatusLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Status.


        :param links: The links of this Status.  # noqa: E501
        :type: StatusLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def battery(self):
        """Gets the battery of this Status.  # noqa: E501


        :return: The battery of this Status.  # noqa: E501
        :rtype: Battery
        """
        return self._battery

    @battery.setter
    def battery(self, battery):
        """Sets the battery of this Status.


        :param battery: The battery of this Status.  # noqa: E501
        :type: Battery
        """

        self._battery = battery

    @property
    def doors_state(self):
        """Gets the doors_state of this Status.  # noqa: E501


        :return: The doors_state of this Status.  # noqa: E501
        :rtype: DoorsState
        """
        return self._doors_state

    @doors_state.setter
    def doors_state(self, doors_state):
        """Sets the doors_state of this Status.


        :param doors_state: The doors_state of this Status.  # noqa: E501
        :type: DoorsState
        """

        self._doors_state = doors_state

    @property
    def energy(self):
        """Gets the energy of this Status.  # noqa: E501

        Describe vehicle energy supply for thermic, low emission vehicle or both.  # noqa: E501

        :return: The energy of this Status.  # noqa: E501
        :rtype: list[Energy]
        """
        return self._energy

    @energy.setter
    def energy(self, energy):
        """Sets the energy of this Status.

        Describe vehicle energy supply for thermic, low emission vehicle or both.  # noqa: E501

        :param energy: The energy of this Status.  # noqa: E501
        :type: list[Energy]
        """

        self._energy = energy

    @property
    def environment(self):
        """Gets the environment of this Status.  # noqa: E501


        :return: The environment of this Status.  # noqa: E501
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Status.


        :param environment: The environment of this Status.  # noqa: E501
        :type: Environment
        """

        self._environment = environment

    @property
    def ignition(self):
        """Gets the ignition of this Status.  # noqa: E501


        :return: The ignition of this Status.  # noqa: E501
        :rtype: Ignition
        """
        return self._ignition

    @ignition.setter
    def ignition(self, ignition):
        """Sets the ignition of this Status.


        :param ignition: The ignition of this Status.  # noqa: E501
        :type: Ignition
        """

        self._ignition = ignition

    @property
    def kinetic(self):
        """Gets the kinetic of this Status.  # noqa: E501


        :return: The kinetic of this Status.  # noqa: E501
        :rtype: Kinetic
        """
        return self._kinetic

    @kinetic.setter
    def kinetic(self, kinetic):
        """Sets the kinetic of this Status.


        :param kinetic: The kinetic of this Status.  # noqa: E501
        :type: Kinetic
        """

        self._kinetic = kinetic

    @property
    def last_position(self):
        """Gets the last_position of this Status.  # noqa: E501


        :return: The last_position of this Status.  # noqa: E501
        :rtype: Position
        """
        return self._last_position

    @last_position.setter
    def last_position(self, last_position):
        """Sets the last_position of this Status.


        :param last_position: The last_position of this Status.  # noqa: E501
        :type: Position
        """

        self._last_position = last_position

    @property
    def preconditionning(self):
        """Gets the preconditionning of this Status.  # noqa: E501


        :return: The preconditionning of this Status.  # noqa: E501
        :rtype: Preconditioning
        """
        return self._preconditionning

    @preconditionning.setter
    def preconditionning(self, preconditionning):
        """Sets the preconditionning of this Status.


        :param preconditionning: The preconditionning of this Status.  # noqa: E501
        :type: Preconditioning
        """

        self._preconditionning = preconditionning

    @property
    def privacy(self):
        """Gets the privacy of this Status.  # noqa: E501


        :return: The privacy of this Status.  # noqa: E501
        :rtype: Privacy
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this Status.


        :param privacy: The privacy of this Status.  # noqa: E501
        :type: Privacy
        """

        self._privacy = privacy

    @property
    def safety(self):
        """Gets the safety of this Status.  # noqa: E501


        :return: The safety of this Status.  # noqa: E501
        :rtype: Safety
        """
        return self._safety

    @safety.setter
    def safety(self, safety):
        """Sets the safety of this Status.


        :param safety: The safety of this Status.  # noqa: E501
        :type: Safety
        """

        self._safety = safety

    @property
    def service(self):
        """Gets the service of this Status.  # noqa: E501


        :return: The service of this Status.  # noqa: E501
        :rtype: ServiceType
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Status.


        :param service: The service of this Status.  # noqa: E501
        :type: ServiceType
        """

        self._service = service

    @property
    def timed_odometer(self):
        """Gets the timed_odometer of this Status.  # noqa: E501


        :return: The timed_odometer of this Status.  # noqa: E501
        :rtype: VehicleOdometer
        """
        return self._timed_odometer

    @timed_odometer.setter
    def timed_odometer(self, timed_odometer):
        """Sets the timed_odometer of this Status.


        :param timed_odometer: The timed_odometer of this Status.  # noqa: E501
        :type: VehicleOdometer
        """

        self._timed_odometer = timed_odometer

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Status, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Status):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

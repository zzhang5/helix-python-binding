# package org.apache.helix
#from org.apache.helix import *

from org.apache.helix.util.misc import enum

ChangeType = enum('IDEAL_STATE', 'CONFIG', 'LIVE_INSTANCE', 'CURRENT_STATE', 'MESSAGE', 'EXTERNAL_VIEW', 'CONTROLLER', 'MESSAGES_CONTROLLER', 'HEALTH')

StateModelToken=enum('ANY_LIVEINSTANCE')

ClusterConfigType = enum('HELIX_DISABLE_PIPELINE_TRIGGERS')

# some zk enums from zkClient. See what it does and map to kazoo
class ZKEventType():
    Nothing=-1
    NodeCreated=1
    NodeDeleted=2
    NodeDataChanged=3
    NodeChildrenChanged=4

class KeeperState():
    #Unused, this state is never generated by the server */
#    @Deprecated
    Unknown=-1

    '''The client is in the disconnected state - it is not connected
       to any server in the ensemble. '''
    Disconnected= 0

    # Unused, this state is never generated by the server
    #@Deprecated
    NoSyncConnected =1

    ''' The client is in the connected state - it is connected
        to a server in the ensemble (one of the servers specified
        in the host connection parameter during ZooKeeper client
        reation). '''
    SyncConnected = 3

    #Auth failed state
    AuthFailed= 4

    ''' The serving cluster has expired this session. The ZooKeeper
         client connection (the session) is no longer valid. You must
     create a new client connection (instantiate a new ZooKeeper
     instance) if you with to access the ensemble. '''
    Expired=-112

class HelixConstants:





    """
    Java modifiers:
         final static
    Type:
        String
    """
    DEFAULT_STATE_MODEL_FACTORY = "DEFAULT"


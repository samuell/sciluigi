'''
Scientific Luigi (SciLuigi for short) is a light-weight wrapper library around
Spotify's Luigi workflow system that aims to make writing scientific workflows
(consisting of numerous interdependent commandline applications) more fluent,
flexible and modular.
'''

from sciluigi import interface
from sciluigi.interface import run
from sciluigi.interface import run_local
from sciluigi.interface import LOGFMT_STREAM
from sciluigi.interface import LOGFMT_LUIGI
from sciluigi.interface import LOGFMT_SCILUIGI
from sciluigi.interface import DATEFMT

from sciluigi import audit
from sciluigi.audit import AuditTrailHelpers

from sciluigi import dependencies
from sciluigi.dependencies import TargetInfo
from sciluigi.dependencies import S3TargetInfo
from sciluigi.dependencies import DependencyHelpers

from sciluigi import parameter
from sciluigi.parameter import Parameter

from sciluigi import slurm
from sciluigi.slurm import SlurmInfo
from sciluigi.slurm import SlurmTask
from sciluigi.slurm import SlurmHelpers
from sciluigi.slurm import RUNMODE_LOCAL
from sciluigi.slurm import RUNMODE_HPC
from sciluigi.slurm import RUNMODE_MPI

from sciluigi import task
from sciluigi.task import new_task
from sciluigi.task import Task
from sciluigi.task import ExternalTask
from sciluigi.workflow import WorkflowTask

from sciluigi import util
from sciluigi.util import timestamp
from sciluigi.util import timepath
from sciluigi.util import recordfile_to_dict
from sciluigi.util import dict_to_recordfile

__all__ = ['interface', 'run', 'run_local', 'LOGFMT_STREAM', 'LOGFMT_LUIGI',
        'LOGFMT_SCILUIGI', 'DATEFMT', 'audit', 'AuditTrailHelpers',
        'dependencies', 'TargetInfo', 'S3TargetInfo', 'DependencyHelpers',
        'parameter', 'Parameter', 'slurm', 'SlurmInfo', 'SlurmTask',
        'SlurmHelpers', 'RUNMODE_LOCAL', 'RUNMODE_HPC', 'RUNMODE_MPI', 'task',
        'new_task', 'Task', 'ExternalTask', 'WorkflowTask', 'util',
        'timestamp', 'timepath', 'recordfile_to_dict', 'dict_to_recordfile']

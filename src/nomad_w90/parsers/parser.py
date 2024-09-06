from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
from nomad.parsing.parser import MatchingParser

from nomad.datamodel.metainfo.workflow import Workflow

from nomad_simulations.schema_packages.general import Simulation, Program

from nomad.parsing.file_parser import Quantity, TextParser, DataTextParser

configuration = config.get_plugin_entry_point(
    'nomad_w90.parsers:parser_entry_point'
)


class NewParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
        child_archives: dict[str, 'EntryArchive'] = None,
    ) -> None:
        logger.info('NewParser.parse', parameter=configuration.parameter)

        simulation = Simulation()
        archive.data = simulation

        program = Program(name='Wannier90')
        simulation.program = program
        print("Hello!")



        #archive.workflow2 = Workflow(name='test')
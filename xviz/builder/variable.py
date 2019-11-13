from xviz.builder.base_builder import XVIZBaseBuilder, CATEGORY
from xviz.v2.core_pb2 import Variable, VariableState

class XVIZVariableBuilder(XVIZBaseBuilder):
    def __init__(self, metadata, validator):
        super().__init__(CATEGORY.POSE, metadata, validator)

        # Stores variable data by stream then id
        # They will then be group when constructing final object
        self._data = {}

        # inflight builder data
        self._id = None
        self._values = None

    def id(self, identifier):
        self.validate_prop_set_once('_id')
        self._id = identifier
        return self

    def values(self, values):
        self.validate_prop_set_once('_values')
        if not isinstance(values, [list, tuple]):
            self.validate_error("Input `values` must be array")

        self._values = values
        return self

    def get_data(self):
        self._flush()
        if not self._data:
            return None

        return self._data

    def _add_variable_entry(self):
        if not self._data_pending():
            return

        entry = Variable()
        value = self._values[0]
        if isinstance(value, str):
            entry.strings.extend(self._values) 
        elif isinstance(value, bool):
            entry.bools.extend(self._values)
        elif isinstance(value, int):
            entry.int32s.extend(self._values)
        elif isinstance(value, float):
            entry.doubles.extend(self._values)
        else:
            self.validate_error("The type of input value is not recognized!")
        if self._id:
            entry.base.object_id = self._id

        if self._stream_id in self._data.keys():
            if self._id in self._data[self._stream_id]:
                self.validate_error("Input `values` already set for id %s" % self._id)
            else:
                self._data[self._stream_id].variables[self._id] = entry
        else:
            id_entry = VariableState()
            id_entry.variables[self._id] = entry
            self._data[self._stream_id] = id_entry

    def _data_pending(self):
        return self._values and self._id

    def _validate(self):
        if self._data_pending():
            super()._validate()
            if self._values is None:
                self.validate_warn("Stream %s values are not provided" % self._stream_id)

    def _flush(self):
        self._validate()
        self._add_variable_entry()
        self._reset()

    def _reset(self):
        self._id = None
        self._values = None

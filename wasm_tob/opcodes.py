"""Defines mappings of opcodes to their info structures."""
from __future__ import print_function, absolute_import, division, unicode_literals

from collections import namedtuple
from .immtypes import *


Opcode = namedtuple('Opcode', 'id mnemonic imm_struct flags')

# Flags describing generic characteristics of instructions
INSN_ENTER_BLOCK = 1 << 0
INSN_LEAVE_BLOCK = 1 << 1
INSN_BRANCH = 1 << 2
INSN_NO_FLOW = 1 << 3  # does not pass control to next insn


OPCODES = [
    Opcode(0x00, 'unreachable',           None,                     INSN_NO_FLOW),
    Opcode(0x01, 'nop',                   None,                     0),
    Opcode(0x02, 'block',                 BlockImm(),               INSN_ENTER_BLOCK),
    Opcode(0x03, 'loop',                  BlockImm(),               INSN_ENTER_BLOCK),
    Opcode(0x04, 'if',                    BlockImm(),               INSN_ENTER_BLOCK),
    Opcode(0x05, 'else',                  None,                     INSN_ENTER_BLOCK | INSN_LEAVE_BLOCK),
    Opcode(0x0b, 'end',                   None,                     INSN_LEAVE_BLOCK),
    Opcode(0x0c, 'br',                    BranchImm(),              INSN_BRANCH),
    Opcode(0x0d, 'br_if',                 BranchImm(),              INSN_BRANCH),
    Opcode(0x0e, 'br_table',              BranchTableImm(),         INSN_BRANCH),
    Opcode(0x0f, 'return',                None,                     INSN_NO_FLOW),

    Opcode(0x10, 'call',                  CallImm(),                INSN_BRANCH),
    Opcode(0x11, 'call_indirect',         CallIndirectImm(),        INSN_BRANCH),

    Opcode(0x1a, 'drop',                  None,                     0),
    Opcode(0x1b, 'select',                None,                     0),

    Opcode(0x20, 'local.get',             LocalVarXsImm(),          0),
    Opcode(0x21, 'local.set',             LocalVarXsImm(),          0),
    Opcode(0x22, 'local.tee',             LocalVarXsImm(),          0),
    Opcode(0x23, 'global.get',            GlobalVarXsImm(),         0),
    Opcode(0x24, 'global.set',            GlobalVarXsImm(),         0),
    # Memory Instructions (https://webassembly.github.io/spec/core/binary/instructions.html#memory-instructions)
    Opcode(0x28, 'i32.load',              MemoryImm(),              0),
    Opcode(0x29, 'i64.load',              MemoryImm(),              0),
    Opcode(0x2a, 'f32.load',              MemoryImm(),              0),
    Opcode(0x2b, 'f64.load',              MemoryImm(),              0),
    Opcode(0x2c, 'i32.load8_s',           MemoryImm(),              0),
    Opcode(0x2d, 'i32.load8_u',           MemoryImm(),              0),
    Opcode(0x2e, 'i32.load16_s',          MemoryImm(),              0),
    Opcode(0x2f, 'i32.load16_u',          MemoryImm(),              0),
    Opcode(0x30, 'i64.load8_s',           MemoryImm(),              0),
    Opcode(0x31, 'i64.load8_u',           MemoryImm(),              0),
    Opcode(0x32, 'i64.load16_s',          MemoryImm(),              0),
    Opcode(0x33, 'i64.load16_u',          MemoryImm(),              0),
    Opcode(0x34, 'i64.load32_s',          MemoryImm(),              0),
    Opcode(0x35, 'i64.load32_u',          MemoryImm(),              0),
    Opcode(0x36, 'i32.store',             MemoryImm(),              0),
    Opcode(0x37, 'i64.store',             MemoryImm(),              0),
    Opcode(0x38, 'f32.store',             MemoryImm(),              0),
    Opcode(0x39, 'f64.store',             MemoryImm(),              0),
    Opcode(0x3a, 'i32.store8',            MemoryImm(),              0),
    Opcode(0x3b, 'i32.store16',           MemoryImm(),              0),
    Opcode(0x3c, 'i64.store8',            MemoryImm(),              0),
    Opcode(0x3d, 'i64.store16',           MemoryImm(),              0),
    Opcode(0x3e, 'i64.store32',           MemoryImm(),              0),
    Opcode(0x3f, 'memory.size',           CurGrowMemImm(),          0),
    Opcode(0x40, 'memory.grow',           CurGrowMemImm(),          0),
    # Numeric Instructions (https://webassembly.github.io/spec/core/binary/instructions.html#numeric-instructions)
    Opcode(0x41, 'i32.const',             I32ConstImm(),            0),
    Opcode(0x42, 'i64.const',             I64ConstImm(),            0),
    Opcode(0x43, 'f32.const',             F32ConstImm(),            0),
    Opcode(0x44, 'f64.const',             F64ConstImm(),            0),

    Opcode(0x45, 'i32.eqz',               None,                     0),
    Opcode(0x46, 'i32.eq',                None,                     0),
    Opcode(0x47, 'i32.ne',                None,                     0),
    Opcode(0x48, 'i32.lt_s',              None,                     0),
    Opcode(0x49, 'i32.lt_u',              None,                     0),
    Opcode(0x4a, 'i32.gt_s',              None,                     0),
    Opcode(0x4b, 'i32.gt_u',              None,                     0),
    Opcode(0x4c, 'i32.le_s',              None,                     0),
    Opcode(0x4d, 'i32.le_u',              None,                     0),
    Opcode(0x4e, 'i32.ge_s',              None,                     0),
    Opcode(0x4f, 'i32.ge_u',              None,                     0),

    Opcode(0x50, 'i64.eqz',               None,                     0),
    Opcode(0x51, 'i64.eq',                None,                     0),
    Opcode(0x52, 'i64.ne',                None,                     0),
    Opcode(0x53, 'i64.lt_s',              None,                     0),
    Opcode(0x54, 'i64.lt_u',              None,                     0),
    Opcode(0x55, 'i64.gt_s',              None,                     0),
    Opcode(0x56, 'i64.gt_u',              None,                     0),
    Opcode(0x57, 'i64.le_s',              None,                     0),
    Opcode(0x58, 'i64.le_u',              None,                     0),
    Opcode(0x59, 'i64.ge_s',              None,                     0),
    Opcode(0x5a, 'i64.ge_u',              None,                     0),

    Opcode(0x5b, 'f32.eq',                None,                     0),
    Opcode(0x5c, 'f32.ne',                None,                     0),
    Opcode(0x5d, 'f32.lt',                None,                     0),
    Opcode(0x5e, 'f32.gt',                None,                     0),
    Opcode(0x5f, 'f32.le',                None,                     0),
    Opcode(0x60, 'f32.ge',                None,                     0),

    Opcode(0x61, 'f64.eq',                None,                     0),
    Opcode(0x62, 'f64.ne',                None,                     0),
    Opcode(0x63, 'f64.lt',                None,                     0),
    Opcode(0x64, 'f64.gt',                None,                     0),
    Opcode(0x65, 'f64.le',                None,                     0),
    Opcode(0x66, 'f64.ge',                None,                     0),

    Opcode(0x67, 'i32.clz',               None,                     0),
    Opcode(0x68, 'i32.ctz',               None,                     0),
    Opcode(0x69, 'i32.popcnt',            None,                     0),
    Opcode(0x6a, 'i32.add',               None,                     0),
    Opcode(0x6b, 'i32.sub',               None,                     0),
    Opcode(0x6c, 'i32.mul',               None,                     0),
    Opcode(0x6d, 'i32.div_s',             None,                     0),
    Opcode(0x6e, 'i32.div_u',             None,                     0),
    Opcode(0x6f, 'i32.rem_s',             None,                     0),
    Opcode(0x70, 'i32.rem_u',             None,                     0),
    Opcode(0x71, 'i32.and',               None,                     0),
    Opcode(0x72, 'i32.or',                None,                     0),
    Opcode(0x73, 'i32.xor',               None,                     0),
    Opcode(0x74, 'i32.shl',               None,                     0),
    Opcode(0x75, 'i32.shr_s',             None,                     0),
    Opcode(0x76, 'i32.shr_u',             None,                     0),
    Opcode(0x77, 'i32.rotl',              None,                     0),
    Opcode(0x78, 'i32.rotr',              None,                     0),

    Opcode(0x79, 'i64.clz',               None,                     0),
    Opcode(0x7a, 'i64.ctz',               None,                     0),
    Opcode(0x7b, 'i64.popcnt',            None,                     0),
    Opcode(0x7c, 'i64.add',               None,                     0),
    Opcode(0x7d, 'i64.sub',               None,                     0),
    Opcode(0x7e, 'i64.mul',               None,                     0),
    Opcode(0x7f, 'i64.div_s',             None,                     0),
    Opcode(0x80, 'i64.div_u',             None,                     0),
    Opcode(0x81, 'i64.rem_s',             None,                     0),
    Opcode(0x82, 'i64.rem_u',             None,                     0),
    Opcode(0x83, 'i64.and',               None,                     0),
    Opcode(0x84, 'i64.or',                None,                     0),
    Opcode(0x85, 'i64.xor',               None,                     0),
    Opcode(0x86, 'i64.shl',               None,                     0),
    Opcode(0x87, 'i64.shr_s',             None,                     0),
    Opcode(0x88, 'i64.shr_u',             None,                     0),
    Opcode(0x89, 'i64.rotl',              None,                     0),
    Opcode(0x8a, 'i64.rotr',              None,                     0),

    Opcode(0x8b, 'f32.abs',               None,                     0),
    Opcode(0x8c, 'f32.neg',               None,                     0),
    Opcode(0x8d, 'f32.ceil',              None,                     0),
    Opcode(0x8e, 'f32.floor',             None,                     0),
    Opcode(0x8f, 'f32.trunc',             None,                     0),
    Opcode(0x90, 'f32.nearest',           None,                     0),
    Opcode(0x91, 'f32.sqrt',              None,                     0),
    Opcode(0x92, 'f32.add',               None,                     0),
    Opcode(0x93, 'f32.sub',               None,                     0),
    Opcode(0x94, 'f32.mul',               None,                     0),
    Opcode(0x95, 'f32.div',               None,                     0),
    Opcode(0x96, 'f32.min',               None,                     0),
    Opcode(0x97, 'f32.max',               None,                     0),
    Opcode(0x98, 'f32.copysign',          None,                     0),
    
    Opcode(0x99, 'f64.abs',               None,                     0),
    Opcode(0x9a, 'f64.neg',               None,                     0),
    Opcode(0x9b, 'f64.ceil',              None,                     0),
    Opcode(0x9c, 'f64.floor',             None,                     0),
    Opcode(0x9d, 'f64.trunc',             None,                     0),
    Opcode(0x9e, 'f64.nearest',           None,                     0),
    Opcode(0x9f, 'f64.sqrt',              None,                     0),
    Opcode(0xa0, 'f64.add',               None,                     0),
    Opcode(0xa1, 'f64.sub',               None,                     0),
    Opcode(0xa2, 'f64.mul',               None,                     0),
    Opcode(0xa3, 'f64.div',               None,                     0),
    Opcode(0xa4, 'f64.min',               None,                     0),
    Opcode(0xa5, 'f64.max',               None,                     0),
    Opcode(0xa6, 'f64.copysign',          None,                     0),

    Opcode(0xa7, 'i32.wrap_i64',          None,                     0),
    Opcode(0xa8, 'i32.trunc_f32_s',       None,                     0),
    Opcode(0xa9, 'i32.trunc_f32_u',       None,                     0),
    Opcode(0xaa, 'i32.trunc_f64_s',       None,                     0),
    Opcode(0xab, 'i32.trunc_f64_u',       None,                     0),
    Opcode(0xac, 'i64.extend_i32_s',      None,                     0),
    Opcode(0xad, 'i64.extend_i32_u',      None,                     0),
    Opcode(0xae, 'i64.trunc_f32_s',       None,                     0),
    Opcode(0xaf, 'i64.trunc_f32_u',       None,                     0),
    Opcode(0xb0, 'i64.trunc_f64_s',       None,                     0),
    Opcode(0xb1, 'i64.trunc_f64_u',       None,                     0),
    Opcode(0xb2, 'f32.convert_i32_s',     None,                     0),
    Opcode(0xb3, 'f32.convert_i32_u',     None,                     0),
    Opcode(0xb4, 'f32.convert_i64_s',     None,                     0),
    Opcode(0xb5, 'f32.convert_i64_u',     None,                     0),
    Opcode(0xb6, 'f32.demote_f64',        None,                     0),
    Opcode(0xb7, 'f64.convert_i32_s',     None,                     0),
    Opcode(0xb8, 'f64.convert_i32_u',     None,                     0),
    Opcode(0xb9, 'f64.convert_i64_s',     None,                     0),
    Opcode(0xba, 'f64.convert_i64_u',     None,                     0),
    Opcode(0xbb, 'f64.promote_f32',       None,                     0),

    Opcode(0xbc, 'i32.reinterpret_f32',   None,                     0),
    Opcode(0xbd, 'i64.reinterpret_f64',   None,                     0),
    Opcode(0xbe, 'f32.reinterpret_i32',   None,                     0),
    Opcode(0xbf, 'f64.reinterpret_i64',   None,                     0),
]

OPCODE_MAP = {x.id: x for x in OPCODES}

# Generate integer constants for opcodes.
for cur_op in OPCODES:
    globals()[
        'OP_' + cur_op.mnemonic.upper().replace('.', '_').replace('/', '_')
    ] = cur_op.id

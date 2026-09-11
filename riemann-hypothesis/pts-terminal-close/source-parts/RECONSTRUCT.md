# Reconstructing `interval_ht.py`

The recovered certifier was 26,709 bytes in the session export and used CRLF line endings.

Original exported-byte SHA-256:

`defcba0e76c937b72aeee655243966fc92b222131c35e18c0863d34c2cd4d9eb`

For GitHub publication the source is preserved in five ordered UTF-8 text parts with LF line endings:

1. `interval_ht.py.part01`
2. `interval_ht.py.part02`
3. `interval_ht.py.part03`
4. `interval_ht.py.part04`
5. `interval_ht.py.part05`

Reconstruct the executable source with:

```bash
cat interval_ht.py.part01 interval_ht.py.part02 interval_ht.py.part03 interval_ht.py.part04 interval_ht.py.part05 > interval_ht.py
python interval_ht.py --selftest
```

The SHA-256 of the original source after CRLF -> LF normalization is expected to be:

`dffaf238d17137fb2215b3a7b78c971ba6767a37696e3075a4510225e51d4346`

The fresh extraction-time self-test receipt is in `../SELFTEST-OUTPUT-2026-09-11.txt`.

The source was split only because the publication connector writes UTF-8 content files one at a time; the split is not a mathematical or software refactor.

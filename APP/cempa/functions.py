from glob import glob

from sqlalchemy import select

from cempa.model import FileHash, session


def get_list_nc(path_files: str) -> list:
    return glob(f"{path_files}/*.nc")


def exists_in_the_bank(file_hash: str) -> bool:
    is_valid = session.execute(
        select(FileHash).where(FileHash.file_hash == file_hash)
    )
    if len(is_valid.fetchall()) > 0:
        return True
    return False


def save_hash(str_hash: str) -> None:
    session.add(FileHash(file_hash=str_hash))
    session.commit()

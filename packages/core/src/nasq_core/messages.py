"""User-facing message catalogue in English and Arabic.

Every message says what happened and how to fix it (Definition of Done, item 7).
"""

from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType
from typing import Literal

type Locale = Literal["en", "ar"]

SUPPORTED_LOCALES: tuple[Locale, ...] = ("en", "ar")
DEFAULT_LOCALE: Locale = "en"


@dataclass(frozen=True, slots=True)
class Message:
    title: str
    detail: str


MESSAGES: Mapping[str, Mapping[Locale, Message]] = MappingProxyType(
    {
        "internal_error": {
            "en": Message(
                "Something went wrong on our side",
                "The server could not complete the request. Try again; if it keeps failing, "
                "contact support and quote the request ID.",
            ),
            "ar": Message(
                "حدث خطأ من جهتنا",
                "تعذّر على الخادم إكمال الطلب. حاول مرة أخرى، وإذا استمر الخطأ "
                "فتواصل مع الدعم واذكر رقم الطلب.",
            ),
        },
        "not_found": {
            "en": Message(
                "Not found",
                "The address you requested does not exist. Check the URL and try again.",
            ),
            "ar": Message(
                "غير موجود",
                "العنوان المطلوب غير موجود. تحقّق من الرابط وحاول مرة أخرى.",
            ),
        },
        "method_not_allowed": {
            "en": Message(
                "Method not allowed",
                "This address does not accept this kind of request. Check the API "
                "documentation for the allowed methods.",
            ),
            "ar": Message(
                "الطريقة غير مسموح بها",
                "هذا العنوان لا يقبل هذا النوع من الطلبات. راجع توثيق الواجهة البرمجية "
                "لمعرفة الطرق المسموح بها.",
            ),
        },
        "validation_failed": {
            "en": Message(
                "The request is not valid",
                "Some fields are missing or have the wrong format. Correct the fields listed "
                "in errors and send the request again.",
            ),
            "ar": Message(
                "الطلب غير صالح",
                "بعض الحقول مفقودة أو بصيغة غير صحيحة. صحّح الحقول المذكورة في قائمة "
                "الأخطاء ثم أعد إرسال الطلب.",
            ),
        },
        "service_not_ready": {
            "en": Message(
                "Service not ready",
                "A component the service needs is not reachable yet. Wait a moment and try "
                "again; operators should check the components marked unavailable.",
            ),
            "ar": Message(
                "الخدمة غير جاهزة",
                "أحد المكوّنات التي تحتاجها الخدمة غير متاح حالياً. انتظر قليلاً ثم حاول "
                "مرة أخرى، وعلى فريق التشغيل فحص المكوّنات المعلَّمة بأنها غير متاحة.",
            ),
        },
        "http_error": {
            "en": Message(
                "The request could not be completed",
                "The server rejected the request. Check the status code and the request, "
                "then try again.",
            ),
            "ar": Message(
                "تعذّر إكمال الطلب",
                "رفض الخادم الطلب. تحقّق من رمز الحالة ومن الطلب ثم حاول مرة أخرى.",
            ),
        },
    }
)


def message_for(code: str, locale: Locale) -> Message:
    """Return the message for a code; unknown codes raise KeyError rather than invent text."""
    return MESSAGES[code][locale]


def negotiate_locale(accept_language: str | None) -> Locale:
    """Pick the supported locale with the highest quality in an Accept-Language header."""
    best: Locale = DEFAULT_LOCALE
    best_quality = 0.0
    for item in (accept_language or "").split(","):
        tag, _, params = item.strip().partition(";")
        primary = tag.strip().lower().split("-", 1)[0]
        quality = _quality(params)
        if quality is None or quality <= best_quality:
            continue
        for locale in SUPPORTED_LOCALES:
            if primary == locale:
                best, best_quality = locale, quality
    return best


def _quality(params: str) -> float | None:
    params = params.strip()
    if not params:
        return 1.0
    name, _, value = params.partition("=")
    if name.strip().lower() != "q":
        return 1.0
    try:
        return float(value)
    except ValueError:
        return None

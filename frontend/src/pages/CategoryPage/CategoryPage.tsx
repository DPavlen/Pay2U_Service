import { ReactElement } from 'react';
import SearchFrom from '../../components/SearchFrom/SearchFrom.tsx';
import { Link, useParams } from 'react-router-dom';
import {} from '../../utils/api/Api.ts';
import { IServiceExtended } from '../../utils/interfaces/interfaces.ts';
import './CategoryPage.scss';
import { useSelectorTyped } from '../../hooks/store.ts';

function CategoryPage(): ReactElement {
  const categoryName = useParams<{ category: string }>().category;
  const categories = useSelectorTyped(
    (state) => state.servicesReducer.categorizedServices
  );
  const categoryInStore = categories.find(
    ({ category }) => category?.slug === categoryName
  );
  const category =
    categoryName === 'popular'
      ? useSelectorTyped((store) => store.servicesReducer.popularServices)
      : categoryInStore;

  function renderSubscriptions() {
    return category?.services.map(
      (service: IServiceExtended, index: number) => {
        const lowestPrice = Math.min(
          ...service.tariff.map((t) => t.tariff_promo_price)
        );

        return (
          <li key={`subscription-${index}`}>
            <Link className="link" to={`/services/${service.id}`}>
              <img src={service.icon_small} alt="" />
              <div className="category-page__decription">
                <h3>{service.name}</h3>
                <p>
                  {lowestPrice === Infinity ? (
                    <span>Недоступен для подписки &#128546;</span>
                  ) : (
                    `От ${lowestPrice} ₽ в месяц`
                  )}
                </p>
              </div>
            </Link>
          </li>
        );
      }
    );
  }

  return (
    <section className="category-page">
      <h1 className="title">
        {category?.category?.name || 'Отсутствует имя категории'}
      </h1>
      <SearchFrom />
      <ul className="category-page__list">{renderSubscriptions()}</ul>
    </section>
  );
}

export default CategoryPage;

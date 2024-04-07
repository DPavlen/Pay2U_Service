import { ReactElement } from 'react';
import './CategoryCatalogPage.scss';
import SearchFrom from '../../components/SearchFrom/SearchFrom.tsx';
import CardsSlider from '../../components/CardsSlider/CardsSlider.tsx';
import { useSelectorTyped } from '../../hooks/store.ts';
import { IServiceCategory } from '../../utils/interfaces/interfaces.ts';
import Loader from '../Loader/Loader.tsx';

function CategoryCatalogPage(): ReactElement {
  const categorizedSubscriptions: IServiceCategory[] = useSelectorTyped(
    (store) => store.servicesReducer.categorizedServices
  );
  const isLoading = useSelectorTyped(
    (store) => store.pageStatesReducer.isLoading
  );

  if (isLoading) {
    return <Loader />;
  } else {
    return (
      <section className="category-catalog">
        <h1 className="title">Все сервисы</h1>
        <SearchFrom />
        {categorizedSubscriptions.map((item, index) => (
          <CardsSlider
            key={`category-${index}`}
            title={`${item.category.name}`}
            cardType="big"
            link={`/services/category/${item.category.slug}/`}
            items={item.services}
            slidesPerView={1.8}
          />
        ))}
      </section>
    );
  }
}
export default CategoryCatalogPage;
